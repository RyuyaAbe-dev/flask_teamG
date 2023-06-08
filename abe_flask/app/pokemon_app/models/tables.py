from pokemon_app import db
from datetime import datetime
from flask_login import UserMixin
import random
from pokemon_app import login_manager

@login_manager.user_loader
def get_user(ident):
  return User.query.get(int(ident))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False, unique=True)
    admin = db.Column(db.String(10), nullable=False, default=False)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)

    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<User id:{} email:{} name:{}>'.format(self.id, self.email, self.name)


class PokemonType(db.Model):

    __tablename__ = 'pokemon_types'

    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'), primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), primary_key=True)
    
    def __init__(self, pokemon_id=None,type_id=None):
        self.pokemon_id = pokemon_id
        self.type_id = type_id

    def __repr__(self):
        return '<pokemon_id:{} type_id:{}>'.format(self.pokemon_id, self.type_id)

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(120))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    status = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)
    special_attack = db.Column(db.Integer)
    special_defence = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    legend = db.Column(db.String(10), nullable=False, default=False)
    catch_rate = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
   
    types = db.relationship(
        'Type',
        secondary=PokemonType.__tablename__,
        back_populates='pokemons',
    )

    def __init__(self, name=None, description=None, image=None,height=None,weight=None,status=None,hp=None,attack=None,defence=None,special_defence=None
                 ,special_attack=None,speed=None,legend=None,catch_rate=None):
        self.name = name
        self.description = description
        self.image = image
        self.height = height
        self.weight = weight
        self.status = status
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.special_attack = special_attack
        self.special_defence = special_defence
        self.speed = speed
        self.legend = legend
        self.catch_rate = catch_rate
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Pokemon id:{} name:{} description:{}>'.format(self.id, self.name, self.description)

class Type(db.Model):

    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    pokemons = db.relationship(
        'Pokemon',
        secondary=PokemonType.__tablename__,
        back_populates='types',
    )
     
    def __init__(self,name=None):
        self.name = name
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Type id:{} name:{} >'.format(self.id, self.name)

