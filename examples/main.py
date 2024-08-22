import socket

sock = socket.socket()
addrinfos = socket.getaddrinfo('192.168.178.161', 65432)
sock.connect(addrinfos[0][4])

sock.send("Hallo André")

sock.close()
