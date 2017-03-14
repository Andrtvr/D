import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(10)
while True:
    conn, addr = s.accept()
    path = conn.recv(512).decode('utf8').rstrip("\r\n")
    file = open('/www' + str(path), 'r')
    data = file.read().encode('utf8')
    conn.sendall(data)
    file.close(); conn.close()



readsocks, writesocks = [...], [...] # сокеты
while True:
readables, writeables, exceptions = \
select(readsocks, writesocks, [])
for sockobj in readables:
data = sockobj.recv(512)
if not data:
sockobj.close()
readsocks.remove(sockobj)
else:
print('\tgot', data, 'on', id(sockobj))
