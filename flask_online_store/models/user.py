from . import db, addTimeToModel
from ..utils.encrypt import encrypt

@addTimeToModel
class User(db.Model):
    __tablename__ = 'users'

    id        = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False)
    email     = db.Column(db.String(80), nullable=False)
    password  = db.Column(db.String(255), nullable=False)
    roles     = db.Column(db.JSON, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    token     = db.Column(db.String(255), nullable=False)
    phone     = db.Column(db.String(20))

    # relations
    orders = db.relationship('Order', back_populates='user', lazy='dynamic')
    user_addresses = db.relationship('UserAddress', back_populates='user', lazy='dynamic')

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def serialize(self, user_id):
        dicts = {}
        dicts['is_self'] = True if user_id == self.id else False
        dicts['id'] = self.id
        dicts['username'] = self.username
        dicts['email'] = self.email

        if user_id == self.id:
            dicts['phone'] = self.phone
            dicts['roles'] = self.roles

        return dicts

    def save(self, args):
        self.username = args['username']
        self.password = encrypt(args['password'])
        self.email = args['email']
        self.phone = args['phone']
        self.is_active = True
        self.token = 'init'
        self.roles = ['ROLE_USER']

        db.session.add(self)
        db.session.commit()

    def reset_password(self, new_password):
        pass
