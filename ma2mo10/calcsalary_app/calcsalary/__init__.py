from flask import Flask

# アプリケーションの実体
app = Flask(__name__)
app.config.from_object('calcsalary.config')
from calcsalary import views