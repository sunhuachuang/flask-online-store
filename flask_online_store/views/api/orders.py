from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_restful import Resource

class Order(Resource):
    def get(self, id=None):
        return {'test': 'hello, word from product'}

    def post(self, id=None):
        return {'test': 'hello, word from product'}

    def put(self, id=None):
        return {'test': 'hello, word'}

    def delete(self, id=None):
        return {'test': 'hello, word'}
