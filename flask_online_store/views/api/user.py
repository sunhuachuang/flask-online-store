from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
from flask_restful import Resource
from flask_login import current_user, login_user, login_required

from ...models import User
from ...restparsers.register_parser import register_parser


class UserView(Resource):
    def post(self, id=None):
        args = register_parser.parse_args()
        user = User()
        user.save(args)

        # auto login
        login_user(user)

        return {'token': session['_id']}, 200

    def get(self, id=None):
        user = User.query.get_or_404(user_id)
        return user.serialize(session['id'])

    def put(self, id=None):
        pass

    def delete(self, id=None):
        pass
