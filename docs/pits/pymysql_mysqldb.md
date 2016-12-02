Flask-SQLAlchemy包默认使用的是[MYSQL-python](https://github.com/farcepest/MySQLdb1)包.  
显然这个包已经两年多没有更新了， 所以已经是一个死包了， 而且只支持到2.7版本。  
现在还有一个包[pymysql](https://github.com/PyMySQL/PyMySQL)， 这才是未来啊。  
使用pymysql包只需将config.py里面的:
```
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/fos'
```
改为

```
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/fos'
```
这个包支持 2 ~ 3.5.
