from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_login import requires_login

admin_products = Blueprint('admin_products', __name__)

@admin_products.route('/')
@requires_login
def index():
    pass

@admin_products.route('/new', methods=['GET', 'POST'])
@requires_login
def new():
    pass

@admin_products.route('/edit', methods=['GET', 'POST'])
@requires_login
def edit():
    pass
