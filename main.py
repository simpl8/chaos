from flask import Flask
from settings import Config


app = Flask(__name__)
app.config.from_object(Config)


from users.views import users_blue
app.register_blueprint(users_blue, )



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1908)