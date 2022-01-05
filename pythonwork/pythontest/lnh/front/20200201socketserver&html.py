import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen(5)

while 1:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    print('data=', data.decode('utf8'))
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(b'hello world!')
    conn.send(b'<h1>hello world!</h1>')
    with open('index.html', mode='rb') as f:
        msg = f.read()
    conn.send(msg)


    conn.close()

