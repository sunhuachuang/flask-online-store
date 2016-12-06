from flask import Blueprint, session, redirect, request
from flask_restful import Resource
from flask_login import current_user, login_user, logout_user, login_required

from ...models import User
from ...utils.encrypt import decrypt
from ...restparsers.login_parser import login_parser

class LoginView(Resource):
    def post(self):
        args = login_parser.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user:
            if decrypt(args['password'], user.password):
                login_user(user)

                return {'token': session['_id']}, 200
            else:
                return {'message': {'password': 'password is wrong' }}, 400
        else:
            return {'message': { 'username': 'no user' }}, 400

    def get(self):
        return {'test': 'test'}

class LogoutView(Resource):
    @login_required
    def get(self):
        logout_user()
        return {'status': 200}
