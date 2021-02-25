from flask import Flask, request, render_template, jsonify
import json
from flask_cors import cross_origin
from loguru import logger
#from views import app
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key="akdfhaksdfhaf"

class DbConfig:
    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Suhang1908@182.254.241.179:3306/simple_dev?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


app.config.from_object(DbConfig)
db = SQLAlchemy(app)


# 用户信息(注册的邮箱，密码)
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    email = db.Column(db.String(64), index=True, comment="注册邮箱")
    password = db.Column(db.String(64), nullable=False, comment="密码")


    def __repr__(self):
        return f"{self.email}"


@app.route('/index')
def index():
    return "ok"


@app.route("/api/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        verify_password = request.json.get("verifyPassword")
        if password == verify_password:
            # 注册信息
            reg = User(email=email, password=password)
            db.session.add(reg)
            db.session.commit()
            msg = {"code": 0, "msg": "注册成功"}
            return jsonify(msg)
        else:
            err_msg = {"code": 1, "msg": "输入密码不一致,请重新输入"}
            logger.debug(err_msg)
            return jsonify(err_msg)


@app.route("/api/login", methods=['get', 'post'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        logger.info(username)
        logger.info(password)
    return None


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1908, debug=True)


