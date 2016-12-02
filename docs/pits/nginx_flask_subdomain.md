# 使用nginx反向代理时候的域名前缀的坑
如果想要设置网站的访问为 api.example.com, admin.example.com, example.com。 最简单的方式就是用nginx来做反向代理。  
example.com主要就是传输静态的文件的地址。 主要是主页面和css, js。 可以直接使用nginx获取静态资源， 效率十分高。  
api.exmaple.com 和 admin.example.com 则需要代理指向python去执行。 坑出现了。
```
server {
        listen 80;
        server_name api.fos.dev;
        server_name admin.fos.dev;

        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_read_timeout 86400s;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
}
```
本来是这样配置的nginx, 这时候， flask获取到的server_name 其实是 127.0.0.1:5000这个东西， 但是这个东西无法添加subdomain. 也就是无法这样显示：  
api.127.0.0.1:9000, admin.127.0.0.1:9000  
因此这儿需要对nginx做一些配置上的调整。

```
server {
        listen 80;
        server_name api.fos.dev;
        server_name admin.fos.dev;

        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_read_timeout 86400s;
            proxy_http_version 1.1;
            proxy_set_header Host            $host;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
}
```
添加了
```
proxy_set_header Host            $host;
proxy_set_header X-Forwarded-For $remote_addr;
```
将nginx接受到的 server_name 传递过去。  
此时也必须设置flask的SERVER_NAME参数， 即config.py文件里面的SERVER_NAME = 'fos.dev'.  
这样就可以大功告成了。

