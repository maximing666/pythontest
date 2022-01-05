import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

sk.send(b'hello,server.')
ret = sk.recv(1024)
print(ret)

sk.close()