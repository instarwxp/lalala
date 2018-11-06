# -*- coding: utf-8 -*-
SERVER_PORT = 5000
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = 'helloworld'

IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]