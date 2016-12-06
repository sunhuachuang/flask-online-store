from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_restful import Resource

from ...models import User

class User(Resource):
    def post(self, id=None):
        pass

    def get(self, id=None):
        user = User.query.get_or_404(user_id)
        return user.serialize(session['id'])

    def put(self, id=None):
        pass

    def delete(self, id=None):
        pass
