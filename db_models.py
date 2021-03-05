from views import app
from flask_sqlalchemy import SQLAlchemy
from aes import PrpCrypt
from loguru import logger


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


if __name__ == "__main__":
    # content = PrpCrypt("Suhang1908261908")
    # email = db.session.execute("select email, password from User where email='simple@126.com'").fetchall()
    # db.session.commit()
    # db_email, db_password = email[0][0], email[0][1]
    # logger.info(db_email)
    # logger.info(content.decrypt(db_password))
    

    # password = AES.decrypt(b_email)
    # logger.info(password)
    with app.app_context():
        db.create_all()
        #db.drop_all()