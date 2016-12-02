from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_login import requires_login

admin_orders = Blueprint('admin_orders', __name__)

@admin_orders.route('/')
@requires_login
def index():
    pass

@admin_orders.route('/new', methods=['GET', 'POST'])
@requires_login
def new():
    pass

@admin_orders.route('/edit', methods=['GET', 'POST'])
@requires_login
def edit():
    pass
