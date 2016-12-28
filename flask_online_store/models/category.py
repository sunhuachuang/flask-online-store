from . import db, addTimeToModel

@addTimeToModel
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    products = db.relationship('Product', back_populates='category', lazy='dynamic')
