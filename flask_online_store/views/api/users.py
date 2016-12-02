from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_login import requires_login

api_users = Blueprint('api_users', __name__)

@api_users.route('/me')
@requires_login
def me():
    pass

@api_users.route('/logout')
def logout():
    pass

@api_users.route('/login', methods=['GET', 'POST'])
def login():
    pass
