# 并行工作进程数
workers = 2
# 指定每个工作者的线程数
threads = 4
# 监听内网端口
bind = "0.0.0.0:5000"
# 工作模式协程
worker_class = "gevent"
# 设置最大并发量
worker_connections = 2000
# 设置日志记录水平
loglevel = "debug"
# 代码发生变化是否自动重启
reload = True
accesslog = "./logs/gunicorn.access.log"  # 访问日志文件
errorlog = "./logs/gunicorn.error.log"  # 错误日志文件
