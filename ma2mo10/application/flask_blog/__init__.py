from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# アプリケーション本体
app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

import flask_blog.views