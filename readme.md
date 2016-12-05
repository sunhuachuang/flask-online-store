# flask 开发一个简易的网上商城 (预计一个月左右基本功能实现)

### [文档与坑实时更新](https://github.com/sunhuachuang/flask-online-store/tree/master/docs)

### 特点
1. 前台全部采用api接口的方式（json形式交互）。 后台采用传统的渲染web页面的方式。
2. 目录结构采用功能式的分层结构。[flask项目的结构浅议](https://github.com/sunhuachuang/sun-blog/blob/master/program/flask/flask-dir.md)
3. 服务端（debine/ubuntu）选型: 最前端是nginx, 其后是gunicorn。
4. python版本3.5 (2.7也适用)。
5. 集成支付宝，微信的支付。
6. 将遇到并解决web开发中常见的大部分场景。  
   登录/注册,  
   邮件,  
   验证,  
   事件监听,  
   异常处理,  
   orm,  
   session管理,  
   cache,  
   文件上传下载,  
   安全保证,  
   在线支付,  
   日志管理,  
   性能提升,  
   预留分布式架构  
   ...

### 构建步骤
1. pip3 install -r requirements.txt
2. 配置nginx_flask_online_store.config文件, 设置hosts解析到本地 127.0.0.1 fos.dev api.fos.dev admin.fos.dev
3. 在instance文件下新建config.py文件， 填写个人隐私配置， 覆盖最外层的config.py
4. 配置mysql(默认采用mysql, [可选数据库](http://flask-sqlalchemy.pocoo.org/2.1/config/))
5. python manage.py db_create #新建数据库
6. python manage.py schema_create #新建表
...

### roadmap
1. 基本目录结构 --ok
2. 基本views(路径) --dev
3. 数据库与表的设计 --dev
4. user处理 --waiting
5. products --waiting
6. orders   --waiting
7. paying   --waiting
8. server_config --waiting
9. ...

### 使用到的包
1. Flask(0.11)
2. Flask-Admin
3. Flask-Login
4. Flask-SqlAlchemy
5. Flask-DebugToolbar
6. Flask-Cache
7. gunicorn
8. ...

#### 急速添加中...
