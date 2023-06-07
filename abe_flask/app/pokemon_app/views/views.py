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

@app.route('/search', methods=['POST'])
def search():
    error = None
    print("aaa")
    name = request.form['name']
    number = request.form['number']
    types = request.form.getlist('checkbox')
    return render_template('index.html')