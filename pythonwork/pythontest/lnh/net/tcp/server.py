import socket

sk = socket.socket()             # 买手机
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # 避免服务重启时，报address already in use.
# sk.bind('ip', 端口)
sk.bind(('127.0.0.1', 8080))     # 绑定手机卡
sk.listen()                      # 监听来电

conn, addr = sk.accept()         # 接收来电。conn获取链接，addr获取对方地址
print('client\'s addr:', addr)
ret = conn.recv(1024)            # 获取对方的来电内容。必须是1024的整数倍
print(ret)
conn.send(b'hi,client.')         # 发送信息

conn.close()                     # 关闭监听
sk.close()                       # 关机
