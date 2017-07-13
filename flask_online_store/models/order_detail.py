from . import db, addTimeToModel


@addTimeToModel
class OrderDetail(db.Model):
    __tablename__ = 'order_details'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.SmallInteger)
    amount = db.Column(db.Numeric(10, 2))

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # relations
    order = db.relationship("Order", back_populates="order_details")
    product = db.relationship("Product", back_populates="order_details")
