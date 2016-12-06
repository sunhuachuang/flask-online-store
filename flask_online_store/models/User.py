from . import db, addTimeToModel

@addTimeToModel
class User(db.Model):
    __tablename__ = 'users'

    id        = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False)
    email     = db.Column(db.String(80), unique=True, nullable=False)
    salt      = db.Column(db.String(255), nullable=False)
    password  = db.Column(db.String(255), nullable=False)
    roles     = db.Column(db.JSON, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    token     = db.Column(db.String(255), nullable=False)
    phone     = db.Column(db.String(20))
    qq        = db.Column(db.String(20))

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
            dicts['qq'] = self.qq
            dicts['roles'] = self.roles

        return dicts
