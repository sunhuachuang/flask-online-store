from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_user = Blueprint('admin_user', __name__)

@admin_user.route('/')
def index():
    return 'hello, users'

@admin_user.route('/new', methods=['GET', 'POST'])
def new():
    pass

@admin_user.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
