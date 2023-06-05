from ec_app import db
from datetime import datetime
from flask_login import UserMixin

from ec_app import login_manager

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