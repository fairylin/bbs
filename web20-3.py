"""
性能
1. web性能 选择的并不是性能最高的语言 节省服务器
2. web性能组成
    如：访问百度，查询一个字段

    1.发送request
    2.到达负载均衡
    3.到达nginx
    4.到达web server gunicorn
    5.发送了你的web server app
    6.web server app做了各种事情 返回response

    服务器处理的时间
    7.动态产生一堆页面 客户端渲染

3. 性能本省以后评测标准
    1. 说明硬件，某种网络设备（硬件需要说明）
    2. 性能测试的时候切记方法
        1. benchmark程序已经跑满，app没有跑满
        2. 多个客户端，每个客户端可能有几个链接
    3. 指标 每秒处理多少个请求

    框架作者喜欢测试hello world 因为主要测试本身的解析速度等内容，没有什么页面

4. ab工具  apache benchmark
    安装 apt-get install apache2-utils

重启bbs
supervisorctl restart bbs

ab -n 10 -c 4 http://103.224.82.65/topic/
"""

"""
测试case
1. 需要模拟有性能瓶颈的情况，topic all 做一下sleep
2. 优化方法 cache
    a. 一个操作耗时，结果做cache 保存下来，下次就快些
    b. cache 非永久有效，topic来说，每次修改的时候cache失效
    c. 每次失效时，更新cache

1. 我们可以用内存 cache
2. 我们不使用内存，我们使用redis

1. 发现问题点
2. 根据问题点去做bench
3. 做cache
4. 注意安全
    ufw status verbose
"""