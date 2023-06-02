from flask import Flask

app = Flask(__name__)

app.config.from_object('calcsalary.config')
from calcsalary import views