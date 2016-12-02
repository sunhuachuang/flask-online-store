from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache

cache = Cache()
db = SQLAlchemy()

#from .Category import Category
#from .Product import Product
#from .Order import Order
from .User import User
