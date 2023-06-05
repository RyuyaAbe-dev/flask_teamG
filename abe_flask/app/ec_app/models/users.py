from ec_app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    name = db.Column(db.Text, nullable=False, unique=True)
    admin = db.Column(db.String(10), nullable=False, default=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, email=None, name=None):
        self.email = email
        self.name = name
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<User id:{} email:{} name:{}>'.format(self.id, self.email, self.name)