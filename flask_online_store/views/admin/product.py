from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_product = Blueprint('admin_product', __name__)

@admin_product.route('/')
def index():
    return 'this is admin'

@admin_product.route('/new', methods=['GET', 'POST'])
def new():
    pass

@admin_product.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
