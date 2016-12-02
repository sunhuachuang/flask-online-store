from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_login import requires_login

admin_users = Blueprint('admin_users', __name__)

@admin_users.route('/')
@requires_login
def index():
    pass

@admin_users.route('/new', methods=['GET', 'POST'])
@requires_login
def new():
    pass

@admin_users.route('/edit', methods=['GET', 'POST'])
@requires_login
def edit():
    pass
