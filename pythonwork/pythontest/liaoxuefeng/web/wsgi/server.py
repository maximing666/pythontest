# __*__ coding:utf-8 __*__
from wsgiref.simple_server import make_server
# 导入编写的application函数
from hello import application


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
