from pokemon_app import db
from pokemon_app.models.tables import Pokemon,Type
import random
from flask import request, redirect, url_for, render_template, flash, session
from pokemon_app import app

@app.route('/')
def show_pokemons():
    pokemons = Pokemon.query.order_by(Pokemon.id.asc()).all()
    types = Type.query.order_by(Type.id.asc()).all()
    return render_template('pokemons/index.html', pokemons=pokemons, types=types)