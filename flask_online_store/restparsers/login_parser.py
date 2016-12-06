from flask_restful import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, nullable=False, help="username cannot be blank!")
login_parser.add_argument('password', required=True, nullable=False, help="password cannot be blank!")
