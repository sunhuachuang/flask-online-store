from flask import Blueprint, render_template, redirect, url_for, request, flash, g
from flask_login import login_required

from ...models import Product, ProductImage, db_save
from ...forms.admin.product import ProductForm
from ...forms.admin.product_image import MultiProductImageForm

admin_product = Blueprint('admin_product', __name__)

@admin_product.route('/')
@login_required
def index():
    return render_template('admin/product/index.html', products=Product.query.all())

@admin_product.route('/<id>/images', methods=['GET', 'POST'])
@login_required
def image(id):
    product = Product.query.get_or_404(id)
    form = MultiProductImageForm()

    if request.method == 'POST' and form.validate_on_submit:
        product.save_product_images(form.images.data)
        flash('edit success', 'success')
        return redirect(url_for('admin_product.image', id=id))

    return render_template('admin/product/image.html', product=product, form=form)

@admin_product.route('/images/delete/<id>')
@login_required
def delete_image(id):
    product_image = ProductImage.query.get_or_404(id)
    product_id = product_image.product_id
    product_image.delete_image()

    flash('delete success', 'success')
    return redirect(url_for('admin_product.image', id=product_id))

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
