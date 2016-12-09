from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_category = Blueprint('admin_category', __name__)

@admin_category.route('/')
def index():
    pass

@admin_category.route('/new', methods=['GET', 'POST'])
def new():
    pass

@admin_category.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
