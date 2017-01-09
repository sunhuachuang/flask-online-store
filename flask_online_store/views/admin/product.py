from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from ...models import Product, db_save
from ...forms.admin.product import ProductForm

admin_product = Blueprint('admin_product', __name__)

@admin_product.route('/')
@login_required
def index():
    return render_template('admin/product/index.html', products=Product.query.all())

@admin_product.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    pass

@admin_product.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    pass

def handle_new_and_edit(product):
    pass
