from flask import Flask, request, render_template, jsonify
import json
#from flask_cors import cross_origin
from loguru import logger
#from views import app
from flask_sqlalchemy import SQLAlchemy
from aes import PrpCrypt



app = Flask(__name__)
app.secret_key="akdfhaksdfhaf"
key = "Suhang1908261908"

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
    password = db.Column(db.String(128), nullable=False, comment="密码")


    def __repr__(self):
        return f"{self.email}"


@app.route('/index')
def index():
    return "ok"


@app.route("/api/register", methods=["get", "post"])
def register():
    logger.info(request.method)
    if request.method == "GET":
        return render_template("users/login.html")
    elif request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        verify_password = request.json.get("verifyPassword")
        # AES加密密码
        _AES = PrpCrypt(key)
        if password != "" and verify_password != "" and password == verify_password:
            # 注册信息
            enter_password = _AES.encrypt(password).decode("utf-8")
            reg = User(email=email, password=enter_password)
            db.session.add(reg)
            db.session.commit()
            msg = {"code": 0, "message": "注册成功"}
            logger.info(msg)
            return jsonify(msg)
        elif password == "" or verify_password == "":
            msg = {'code': 1, "message": "密码不能为空"}
            logger.debug(msg)
            return jsonify(msg)
        else:
            msg = {"code": 2, "message": "输入密码不一致,请重新输入"}
            logger.debug(msg)
            return jsonify(msg)


@app.route("/api/login", methods=['get', 'post'])
def login():
    _AES = PrpCrypt(key)
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.json.get('email')
        password = request.json.get('password')
        aes_password = _AES.encrypt(password)
        query_password = db.session.execute("select password from User where email='s1mp1e@126.com'").fetchall()
        db.session.commit()
        real_password = "".join(query_password[0])
        if aes_password == real_password:
            msg = {"code": 0, "msg": "登录成功"}
            return jsonify(msg)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1908, debug=True)


