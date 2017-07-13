from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

admin_order = Blueprint('admin_order', __name__)


@admin_order.route('/')
def index():
    pass


@admin_order.route('/new', methods=['GET', 'POST'])
def new():
    pass


@admin_order.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
