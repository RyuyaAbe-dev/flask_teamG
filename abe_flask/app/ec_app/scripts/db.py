from flask_script import Command
from ec_app import db
from ec_app.models.users import User

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()