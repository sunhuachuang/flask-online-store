from . import db, addTimeToModel

@addTimeToModel
class UserAddress(db.Model):
    __tablename__ = 'user_addresses'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    phone   = db.Column(db.String(20))
    receiver = db.Column(db.String(20))
    zip_code = db.Column(db.String(7))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relations
    user = db.relationship("User", back_populates="user_addresses")
    orders = db.relationship('Order', backref='user_address', lazy='dynamic')
