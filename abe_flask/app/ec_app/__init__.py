from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ec_app.config')

db = SQLAlchemy(app)
from ec_app.views import views