from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# アプリケーション本体
app = Flask(__name__)
app.config.from_object('spl_app.config')

db = SQLAlchemy(app)

from spl_app.views import views