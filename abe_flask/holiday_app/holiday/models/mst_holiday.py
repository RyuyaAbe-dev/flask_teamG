from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holidays'
    holi_date= db.Column(db.DateTime, primary_key=True)
    holi_text = db.Column(db.Text)

    def __init__(self, date=None, text=None):
        self.holi_date = date
        self.holi_text = text


    def __repr__(self):
        return '<holiday text:{}>'.format(self.text)