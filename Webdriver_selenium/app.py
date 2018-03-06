from flask import Flask

app = Flask(__name__)


@app.route("/")  # 路由
def hello():
    return "Hello world!"
