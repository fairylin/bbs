"""
0. web server app
1. web server framework
2. http server
3. tcp server

nginx : http server
gunicorn : http server
wsgi : 包装出来的一个app

nginx gunicorn 是否重复
data -> nginx -> gunicorn -> wsgi -> app

1. 反向代理
    gunicorn 2000
    gunicorn 2002
    nginx 80

2. 负载均衡
    haproxy 去访问google.com

3. 静态文件托管
    本地图片（用户图片上传等）访问速度快，性能不好
    send_by_directory 每次都send太消耗
    配置一个rule 保存在nginx 的缓存，不会走到app这一层

4. 缓冲
    traffic busy
    缓冲负载
"""

"""
上传图像
1. 前端form 
2. post方法，对应路由，处理图片保存
    1.文件后缀需要过滤  防止js  - img png gif jpg
    2.文件名称也要小心
    /var/img
    ../../var... -> XXX
    ~/.bash_rc
    ~/.bash_profile
3. get方法，获取本地的静态文件，转发给用户


发私信
1. id
2. content
3. title
4. sender_id  # 不能从表单中取， 即使hidden（可以被伪造）
5. receiver_id
6. read
"""

