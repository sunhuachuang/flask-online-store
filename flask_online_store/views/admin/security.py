from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_login import current_user, login_user, logout_user, login_required

from ...models import Admin
from ...utils.encrypt import decrypt
from ...forms.admin import LoginForm, RegisterForm

admin_security = Blueprint('admin_security', __name__, static_folder='static', static_url_path='/static')

@admin_security.route('/')
@login_required
def index():
    return render_template('admin/homepage.html')

@admin_security.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Admin.query.filter_by(username=username).first()
        if user:
            if decrypt(password, user.password):
                #login_user(user)
                return redirect(url_for('admin_security.index'))
            else:
                flash('password is wrong!')
        else:
            flash('no user')

    return render_template('admin/login.html', form=form)

@admin_security.route('/logout')
@login_required
def logout():
    logout_user()
    redirect(url_for('admin_security.login'))
