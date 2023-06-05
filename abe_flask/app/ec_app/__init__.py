from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('ec_app.config')

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
from ec_app.views import views, users