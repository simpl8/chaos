# coding=utf-8
# name: simple
from flask import Flask, render_template, request, redirect, url_for
from settings import Config
from loguru import logger


app = Flask(__name__)
app.config.from_object(Config)


# 返回纯文本
@app.route('/api/hello')
def hello():
    logger.info(request.args.get("name"))
    return "helloWorld!"


# 返回html页面
@app.route('/api/hello_form', methods=["get", "post"])
def hello_form():
    if request.method == "GET":
        logger.info(request.args.get("name"))
        return render_template("demon/demon.html")
    elif request.method == "POST":
        args_1 = request.form.get("firArg")
        args_2 = request.form.get("secArg")
        logger.info(args_1)
        logger.info(args_2)
        return render_template('demon/demon.html', args_1=args_1, args_2=args_2)


# url_for重定向
@app.route("/api/redirect")
def hello_redirect():
    # 重定向到具体url地址
    # return redirect("http://www.baidu.com")
    return redirect(url_for("hello_form"))

if __name__ == "__main__":
    # 运行时加载属性
    # app.run(host="127.0.0.1", port=1908, debug=True)
    app.run(host="127.0.0.1", port=1908)