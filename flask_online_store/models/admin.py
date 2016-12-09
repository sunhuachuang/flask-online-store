from . import db, addTimeToModel
from ..utils.encrypt import encrypt

@addTimeToModel
class Admin(db.Model):
    __tablename__ = 'admins'

    id        = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False)
    email     = db.Column(db.String(80), nullable=False)
    password  = db.Column(db.String(255), nullable=False)
    roles     = db.Column(db.JSON, nullable=False)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def save(self, args):
        self.username = args['username']
        self.password = encrypt(args['password'])
        self.email = args['email']
        self.roles = args['roles'] if 'roles' in args else ['ROLE_ADMIN']

        db.session.add(self)
        db.session.commit()

    def reset_password(self, new_password):
        pass
