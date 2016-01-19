import socket, ssl, hashlib, time
CERT="fingerprint que voce pegou"
sock = socket.socket()
sock.settimeout(2)
sock.connect(('localhost', 8081))
conn = ssl.wrap_socket(sock)
if hashlib.md5(conn.getpeercert(True)).hexdigest() != CERT:
    conn.close()
    print 'CERT diferente do esperado, tentando me hackearrrrrrr'
else:
    print '200 OK'
    time.sleep(2)
    conn.write('CHUPA ESSA MANGA, WIRESHARK!1!!')
    print 'enviado'
    conn.close()
