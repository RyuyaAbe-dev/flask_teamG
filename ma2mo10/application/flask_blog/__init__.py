from flask import Flask

# アプリケーション本体
app = Flask(__name__)
app.config.from_object('flask_blog.config')

import flask_blog.views