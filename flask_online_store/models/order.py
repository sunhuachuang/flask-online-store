from . import db, addTimeToModel


@addTimeToModel
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(100))
    is_pay = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_address_id = db.Column(db.Integer, db.ForeignKey('user_addresses.id'))

    # relations
    user = db.relationship("User", back_populates="orders")
    user_address = db.relationship("UserAddress", back_populates="orders")
    order_details = db.relationship(
        'OrderDetail', back_populates='order', lazy='dynamic')
