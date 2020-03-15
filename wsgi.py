# encoding:utf8
import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))

# 引入 app.py
import app

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值 必须时 Flask 实例
# 这是规定的套路（协议）

application = app.app

# 这是把代码部署到 apache gunicorn nginx 后面的套路

# 监护程序 守护程序
"""
cat /etc/supervisor/conf.d/todo.conf

[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true


建立一个软连接
ln -s /var/www/bbs/bbs.conf /etc/supervisor/conf.d/bbs.conf

ln -s /var/www/bbs/bbs.nginx /etc/nginx/sites-enabled/bbs
将我们自己设置的bbs.nginx 文件和 /etc/nginx/sites-enabled/bbs 建立软连接之后
我们需要将 /etc/nginx/sites-enabled/文件夹下的default配置文件删除
可以到/etc/nginx中查看nginx.conf查看，nginx中读取的配置文件来源
通过命令 service nginx restart 重启 nginx 服务即可



➜  ~ cat /etc/supervisor/conf.d/bbs.conf

[program:bbs]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2001
--pid /tmp/飙泪og.pid
"""
