# -*- coding:utf-8 -*-

from application import app


from web.interceptors.AuthInterceptor import  *

from web.controls.index import route_index
from web.controls.user.User import route_user
from web.controls.static import route_static
from web.controls.account.Account import route_account
from web.controls.finance.Finance import route_finance
from web.controls.stat.Stat import route_stat
from web.controls.food.Food import route_food
from web.controls.member.Member import route_member

app.register_blueprint(route_index, url_prefix = '/')
app.register_blueprint(route_user, url_prefix = '/user')
app.register_blueprint(route_static, url_prefix = '/static')
app.register_blueprint(route_account, url_prefix = '/account')
app.register_blueprint(route_finance, url_prefix = '/finance')
app.register_blueprint(route_stat, url_prefix = '/stat')
app.register_blueprint(route_food, url_prefix = '/food')
app.register_blueprint(route_member, url_prefix = '/member')