from flask import Flask
from smallp import route_smallp


app = Flask(__name__)
app.register_blueprint(route_smallp, url_prefix = "/smallp")

@app.route('/')
def hello_world():
    return 'hello world'



if __name__ == "__main__":
    app.run()

