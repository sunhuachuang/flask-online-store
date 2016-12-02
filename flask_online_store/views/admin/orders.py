from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_orders = Blueprint('admin_orders', __name__)

@admin_orders.route('/')
def index():
    pass

@admin_orders.route('/new', methods=['GET', 'POST'])
def new():
    pass

@admin_orders.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
