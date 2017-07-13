from flask_script import Manager
from flask_restful import url_for
from flask_online_store import create_app
from flask_online_store.models import db, User, Admin

app = create_app()
manager = Manager(app)


@manager.command
def db_create(force=False):
    if force:
        sql_config = app.config['SQLALCHEMY_DATABASE_URI']
        sql_configs = sql_config.split('/')
        db_name = sql_configs[-1]
        app.config['SQLALCHEMY_DATABASE_URI'] = '/'.join(sql_configs[0:-1])

        db.engine.execute('drop database if exists ' +
                          db_name + ';create database ' + db_name)

        app.config['SQLALCHEMY_DATABASE_URI'] = sql_config
        print('you had create db', db_name)
    else:
        print('you will create db ', db_name, ', add -f/--force to execute')


@manager.command
def schema_create():
    db.create_all()
    print('you had create all tables')


@manager.command
def schema_drop():
    db.drop_all()
    print('you had drop all tables')


@manager.command
def schema_update():
    db.drop_all()
    db.create_all()
    print('you had update all tables')


@manager.command
def list_routes():
    for rule in app.url_map.iter_rules():
        print(rule)


@manager.option('-n', '--number', dest='number', default='10')
def load_users(number):
    for i in range(0, int(number)):
        user = User()
        args = {}
        args['username'] = 'demo' + str(i)
        args['password'] = '123456'
        args['email'] = 'demo' + str(i) + '@example.com'
        args['phone'] = '1234567890'

        try:
            user.save(args)
        except:
            print(args['username'], ' load eror!')
            continue

    print('load over!')


@manager.option('-u', '--username', dest='username', default='admin')
@manager.option('-p', '--password', dest='password', default='admin')
def load_admin(username, password):
    admin = Admin()
    args = {'username': username, 'password': password, 'roles': [
        'ROLE_SUPER_ADMIN'], 'email': 'admin@examle.com'}

    try:
        admin.save(args)
        print('load ok!')
    except:
        print('load error, check!')


if __name__ == '__main__':
    manager.run()
