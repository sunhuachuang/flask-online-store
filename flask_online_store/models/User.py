from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache

db = SQLAlchemy()
cache = Cache()

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Unicode(64))
    user_qq = db.Column(db.Unicode(16))
    user_mail = db.Column(db.Unicode(64))
    password = db.Column(db.Unicode(128))

    def __init__(self, user_name, password):
        self.user_name = user_name
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
