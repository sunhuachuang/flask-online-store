from flask import Blueprint
from flask_restful import Resource, Api
from .api.users import UserView
from .api.orders import OrderView
from .api.products import ProductView
from .api.security import LoginView, LogoutView

from .admin.users import admin_users
from .admin.orders import admin_orders
from .admin.products import admin_products

def register_blueprints(app):

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(UserView, '/users', '/users/<int:id>')
    api.add_resource(OrderView, '/orders', '/orders/<int:id>')
    api.add_resource(ProductView, '/products', '/products/<int:id>')
    api.add_resource(LoginView, '/login')
    api.add_resource(LogoutView, '/logout')

    app.register_blueprint(api_bp, subdomain='api')

    app.register_blueprint(admin_users, subdomain='admin', url_prefix='/users')
    app.register_blueprint(admin_orders, subdomain='admin', url_prefix='/orders')
    app.register_blueprint(admin_products, subdomain='admin', url_prefix='/products')
