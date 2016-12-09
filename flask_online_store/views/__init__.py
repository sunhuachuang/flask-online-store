from flask import Blueprint
from flask_restful import Resource, Api
from .api.user import UserView
from .api.ordes import OrderView
from .api.product import ProductView
from .api.security import LoginView, LogoutView

from .admin.user import admin_user
from .admin.order import admin_order
from .admin.product import admin_product
from .admin.category import admin_category

def register_blueprints(app):

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(UserView, '/users', '/users/<int:id>')
    api.add_resource(OrderView, '/orders', '/orders/<int:id>')
    api.add_resource(ProductView, '/products', '/products/<int:id>')
    api.add_resource(LoginView, '/login')
    api.add_resource(LogoutView, '/logout')

    app.register_blueprint(api_bp, subdomain='api')

    app.register_blueprint(admin_user, subdomain='admin', url_prefix='/users')
    app.register_blueprint(admin_order, subdomain='admin', url_prefix='/orders')
    app.register_blueprint(admin_product, subdomain='admin', url_prefix='/products')
    app.register_blueprint(admin_category, subdomain='admin', url_prefix='/categories')
