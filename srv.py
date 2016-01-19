import socket, ssl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8081))
sock.listen(1)
newsock, fromaddr = sock.accept()
conn = ssl.wrap_socket(newsock, server_side=True, certfile='cert.pem', keyfile='cert.pem')
conn.setblocking(0)
while True:
    try:
        buf = conn.read(512)
        if buf == '':
            break
        else:
            print buf
    except:
        pass
