from flask import Flask
from settings import Config


app = Flask(__name__)
app.config.from_object(Config)


from users.views import users_blue
from epolicy.views import e_policy
app.register_blueprint(users_blue)
app.register_blueprint(e_policy)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1908)