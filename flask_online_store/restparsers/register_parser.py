from flask_restful import reqparse

from . import check
from ..validators import email_regex

register_parser = reqparse.RequestParser()

register_parser.add_argument('username', required=True, nullable=False, help="username cannot be blank!")
register_parser.add_argument('password', required=True, nullable=False, help="password cannot be blank!")
register_parser.add_argument('email', required=True, nullable=False, type=lambda v: check(v, email_regex), help="email cannot be blank!")
register_parser.add_argument('phone', required=True, nullable=False, help="phone cannot be blank!")
