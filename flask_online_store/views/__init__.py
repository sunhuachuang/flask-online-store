from .api.users import api_users
from .api.orders import api_orders
from .api.products import api_products

from .admin.users import admin_users
from .admin.orders import admin_orders
from .admin.products import admin_products

def register_blueprints(app):
    app.register_blueprint(api_users, subdomain='api', url_prefix='/users')
    app.register_blueprint(api_orders, subdomain='api', url_prefix='/orders')
    app.register_blueprint(api_products, subdomain='api', url_prefix='/products')

    app.register_blueprint(admin_users, subdomain='admin', url_prefix='/users')
    app.register_blueprint(admin_orders, subdomain='admin', url_prefix='/orders')
    app.register_blueprint(admin_products, subdomain='admin', url_prefix='/products')
