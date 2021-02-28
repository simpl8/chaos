from . import users_blue
from flask import request, render_template, jsonify
from loguru import logger
from aes import PrpCrypt
from users.user_form import db, User


key = "Suhang1908261908"


@users_blue.route("/api/register", methods=["get", "post"])
def register():
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
            msg = {"code": 0, "message": "注册成功去登录"}
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
        
    
@users_blue.route("/api/login", methods=["post"])
def login():
    if request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        _AES = PrpCrypt(key)
        info = db.session.execute(f"select email, password from User where email='{email}'").fetchall()
        db.session.commit()
        email_info, password_info = info[0][0], info[0][1]
        if email == email_info and password == _AES.decrypt(password_info):
            logger.info(email, password)
            logger.info(email_info, password_info)
            msg = {"code": 0, "message": "登录成功"}
            return jsonify(msg)
        else:
            logger.debug(f"{email}, {password}")
            logger.debug(f"{email_info}, {password_info}")
            msg = {"code": 1, "message": "用户名密码错误"}
            return jsonify(msg)
        

@users_blue.route("/api/index")
def index():
    return render_template("users/index.html")