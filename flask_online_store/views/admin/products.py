from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_products = Blueprint('admin_products', __name__)

@admin_products.route('/')
def index():
    return 'this is admin'

@admin_products.route('/new', methods=['GET', 'POST'])
def new():
    pass

@admin_products.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
