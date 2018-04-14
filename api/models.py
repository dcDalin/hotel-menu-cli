from api import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Menu %d>' % self.id
