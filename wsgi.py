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

"""
