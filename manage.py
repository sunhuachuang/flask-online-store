from flask_script import Manager
from flask_online_store import create_app
from flask_online_store.models import db, User

app = create_app()
manager = Manager(app)

@manager.command
def db_create(force=False):
    if force:
        sql_config = app.config['SQLALCHEMY_DATABASE_URI'];
        sql_configs = sql_config.split('/')
        db_name = sql_configs[-1]
        app.config['SQLALCHEMY_DATABASE_URI'] = '/'.join(sql_configs[0:-1])

        db.engine.execute('drop database if exists '+db_name+';create database '+db_name)

        app.config['SQLALCHEMY_DATABASE_URI'] = sql_config
        print('you had create db for')
    else:
        print('you will create db fos, add -f/--force to execute')

@manager.command
def schema_create():
    db.create_all()
    print('you had create all tables')

@manager.command
def schema_drop():
    db.drop_all()
    print('you had drop all tables')

@manager.option('-u', '--name', dest='name', default='admin')
@manager.option('-p', '--password', dest='password', default='123456')
def create_user(name, password):
    # admin = User(name, generate_password_hash(password))
    # db.session.add(admin)
    # db.session.commit()
    pass


if __name__ == '__main__':
    manager.run()
