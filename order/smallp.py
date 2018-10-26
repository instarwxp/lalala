from flask import Blueprint

route_smallp = Blueprint("smallp_page", __name__)

@route_smallp.route("/")
def index():
    return "smallp index page"
