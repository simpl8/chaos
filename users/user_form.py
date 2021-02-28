from flask_sqlalchemy import SQLAlchemy
from main import app


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
    