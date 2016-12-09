from flask import Blueprint, send_from_directory

admin_static = Blueprint('admin_static', __name__)

@admin_static.route('/js/<path:path>')
def js(path):
    return send_from_directory('static/js', path)

@admin_static.route('/css/<path:path>')
def css(path):
    return send_from_directory('static/css', path)
