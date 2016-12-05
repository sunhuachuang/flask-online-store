from . import db, addTimeToModel

@addTimeToModel
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
