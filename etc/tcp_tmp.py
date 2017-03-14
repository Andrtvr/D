import socket, select
import os, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0:
        data = conn.recv(1024)
        if not data: break
        if data == 'close' or data =='Close': conn.close()
        conn.send(data)
        #print '(child {}) {} : {conn.getpeername(). request)
        conn.close()
        conn.close()
    else:
        conn.close()
s.close()

