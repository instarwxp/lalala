# -*- coding: utf-8 -*-

from application import app
from flask import request, redirect, g
from common.models.User import User
from common.libs.user.userService import UserService
from common.libs.UrlManager import UrlManager
import re

@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return
    
    
    
    user_info= check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
    
    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return
    
    if not user_info:
        return redirect(UrlManager.buildUrl('/user/login'))
    
    return

'''
判断用户是否已经登录
'''

def check_login():
    #获取cookie
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None
    
    if auth_cookie is None:
        return False
    
    auth_info = auth_cookie.split('#')
    #判断cookie长度
    if len(auth_info) != 2:
        return False
    #查询用户信息
    try:
        user_info = User.query.filter_by(uid = auth_info[1]).first()
    except Exception:
        return False
    #判断用户是否存在
    if user_info is None:
        return False
    
    #判断cookie
    if auth_cookie[0] != UserService.geneAuthCode(user_info):
        return False
    
    return user_info
    