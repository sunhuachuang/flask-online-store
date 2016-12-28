from datetime import datetime
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache

cache = Cache()
db = SQLAlchemy()

def db_save(obj):
    if obj.id:
        obj.before_create()
    else:
        obj.before_update()

    db.session.add(obj)
    db.session.commit()

def addTimeToModel(cls):
    def before_create(cls):
        cls.created_at = datetime.now()
        cls.updated_at = datetime.now()

    def before_update(cls):
        cls.updated_at = datetime.now()

    def before_delete(cls):
        cls.updated_at = datetime.now()
        cls.deleted_at = datetime.now()

    #cls.query = BaseQuery.filter_by(deleted_at=None)

    cls.created_at = db.Column(db.DateTime)
    cls.updated_at = db.Column(db.DateTime)
    cls.deleted_at = db.Column(db.DateTime)
    cls.before_create = before_create
    cls.before_update = before_update
    cls.before_delete = before_delete

    return cls

def addOwnAndTimeToModel(cls):
    def before_create(cls):
        cls.created_at = datetime.now()
        cls.updated_at = datetime.now()
        cls.created_by = session['id']
        cls.updated_by = session['id']

    def before_update(cls):
        cls.updated_at = datetime.now()
        cls.updated_by = session['id']

    def before_delete(cls):
        cls.updated_at = datetime.now()
        cls.deleted_at = datetime.now()
        cls.deleted_by = session['id']

    cls.created_by = db.Column(db.Integer)
    cls.updated_by = db.Column(db.Integer)
    cls.deleted_by = db.Column(db.Integer)
    cls.before_create = before_create
    cls.before_update = before_update
    cls.before_delete = before_delete

    return cls


from .user import User
from .user_address import UserAddress

from .category import Category
from .product import Product
from .product_image import ProductImage

from .order import Order
from .order_detail import OrderDetail

from .admin import Admin
