# -*- coding: utf-8 -*-

from application import app
from flask import request

@app.before_request
def before_request():
    pass

'''
判断用户是否已经登录
'''

def check_login():
    cookies = request.cookies
    