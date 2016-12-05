## flask-script包主要用于自定义一些命令行command.
简单的命令行很好写， 值得说的是带参数的命令行.  
第一种是可选单参数（-f, -v, -h）之类的
```
@manager.command
def db_create(force=False):
    pass
```
这段代码中的force参数就是如此， 可以通过 db_create 之后加上 -f/--force赋值True, 否则其他的均为False, 包括直接 python manage.py db_create force

```
@manager.option('-u', '--name', dest='name', default='admin')
@manager.option('-p', '--password', dest='password', default='123456')
def create_user(name, password):
    pass
```
这段代码则是配置多参数的例子， -u/--name 后面输入的均作为name参数， 比如
```
python manage.py create_user -u admin
```

或者
```
python manage.py create_user --name admin
```
