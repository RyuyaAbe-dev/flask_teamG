from pokemon_app import db
from pokemon_app.models.tables import Pokemon,Type,PokemonType
import random
from flask import request, redirect, url_for, render_template, flash, session
from pokemon_app import app
from sqlalchemy import and_, or_, between, func
from sqlalchemy.sql import text, distinct

@app.route('/')
def show_pokemons():
    pokemons = Pokemon.query.order_by(Pokemon.id.asc()).all()
    types = Type.query.order_by(Type.id.asc()).all()
    type_ids = []
    return render_template('pokemons/index.html', pokemons=pokemons, types=types, type_checked=type_ids)

@app.route('/pokemons/<int:id>', methods=['GET'])
def detail_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return render_template('pokemons/show.html', pokemon=pokemon)

@app.route('/search', methods=['POST'])
def search():
    error = None
    types = Type.query.order_by(Type.id.asc()).all()
    name = request.form['name']
    min_num = request.form['min_num']
    max_num = request.form['max_num']
    type_ids = request.form.getlist('checkbox')
    filters = []
    if name:
        filters.append(Pokemon.name.startswith(func.binary(name)))
    if min_num < max_num:
        filters.append(between(Pokemon.id, min_num, max_num))
    if type_ids:
        filters.append(PokemonType.type_id.in_(type_ids))
    pokemons = db.session.query(Pokemon).join(PokemonType, Pokemon.id == PokemonType.pokemon_id).filter(and_(*filters)).all()
    print(pokemons)
    for pokemon in pokemons:
        print(pokemon.name)
    print(type_ids)
    return render_template('pokemons/index.html',pokemons=pokemons, types=types, type_checked=type_ids, name=name)