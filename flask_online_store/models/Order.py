from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache

db = SQLAlchemy()
cache = Cache()

class Order(db.Model):
    __tablename__ = 'orders'
