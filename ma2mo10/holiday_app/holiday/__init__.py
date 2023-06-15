from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# アプリケーション本体
app = Flask(__name__)
app.config.from_object('holiday.config')

db = SQLAlchemy(app)

from holiday.views import views