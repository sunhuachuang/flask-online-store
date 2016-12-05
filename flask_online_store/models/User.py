from . import db, addTimeToModel

@addTimeToModel
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    salt = db.Column(db.String(100))
    password = db.Column(db.Unicode(128))
    roles = db.Column(db.JSON)

    def __init__(self, username, password):
        self.user_name = username
        self.password = password

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def __unicode__(self):
        return self.user_name
