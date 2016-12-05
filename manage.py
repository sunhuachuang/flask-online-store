from flask_script import Manager
from flask_online_store import create_app
from flask_online_store.models import db, User

app = create_app()
manager = Manager(app)

@manager.command
def db_create():
    sql_config = app.config['SQLALCHEMY_DATABASE_URI'];
    app.config['SQLALCHEMY_DATABASE_URI'] = sql_config #'mysql+pymysql://username:password@server/fos' ;

    db.engine.execute('create database fos')

@manager.command
def schema_create():
    db.create_all()

@manager.option('-u', '--name', dest='name', default='admin')
@manager.option('-p', '--password', dest='password', default='123456')
def create_user(name, password):
    # admin = User(name, generate_password_hash(password))
    # db.session.add(admin)
    # db.session.commit()
    pass


if __name__ == '__main__':
    manager.run()
