# -*- coding: utf-8 -*-
from flask import Blueprint,render_template, request, jsonify, make_response
from common.models.User import User
import json
from common.libs.user.userService import UserService
from application import app


route_user = Blueprint( 'user_page',__name__ )


@route_user.route( "/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template( "user/login.html" )
    req = request.values
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    login_name= req['login_name'] if 'login_name' in req else ''
    login_pwd= req['login_pwd'] if 'login_pwd' in req else ''
    #判断用户名
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码'
        return jsonify(resp)
    #判断用户密码
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码'
        return jsonify(resp)

    
    user_info = User.query.filter_by(login_name = login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码'
        return jsonify(resp)
    
    if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = u'请输入正确的用户名和密码-1'
        return jsonify(resp)

    response = make_response(json.dumps({'code': 200, 'msg': '登录成功！'}))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)
    return response




@route_user.route( "/edit" )
def edit():
    return render_template( "user/edit.html" )

@route_user.route( "/reset-pwd" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )