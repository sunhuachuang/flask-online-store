from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from ...models import Category, db_save
from ...forms.admin import CategoryForm

admin_category = Blueprint('admin_category', __name__)

@admin_category.route('/')
@login_required
def index():
    return render_template('admin/category/index.html', categories=Category.query.all())

@admin_category.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    category = Category()
    return handle_new_and_edit(category)

@admin_category.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    category = Category.query.get_or_404(id)
    return handle_new_and_edit(category)

def handle_new_and_edit(category):
    form = CategoryForm(request.form, obj=category)
    if form.validate_on_submit():
        print(category.name)
        db_save(category)
        return redirect(url_for('admin_category.index'))

    return render_template('admin/category/new_and_edit.html', form=form)
