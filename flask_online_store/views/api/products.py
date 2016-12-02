from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort

api_products = Blueprint('api_products', __name__)

@api_products.route('/')
def index():
    return 'hello world'
