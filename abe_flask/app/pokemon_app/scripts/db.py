from flask_script import Command
from pokemon_app import db
from pokemon_app.models.tables import User,Pokemon,PokemonType,Type

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()