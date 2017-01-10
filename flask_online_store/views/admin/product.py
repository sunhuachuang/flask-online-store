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
    product = Product()
    return handle_new_and_edit(product)

@admin_product.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    product = Product.query.get_or_404(id)
    return handle_new_and_edit(product)

def handle_new_and_edit(product):
    isNew = bool(product.id)
    form = ProductForm(request.form, obj=product)
    if form.validate_on_submit():
        db_save(product)
        flash('edit success' if isNew else 'new success', 'success')
        return redirect(url_for('admin_product.index'))

    return render_template('admin/product/new_and_edit.html', form=form)
