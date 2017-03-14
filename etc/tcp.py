import socket, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

#sock = s
# read in socket
def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        #conn, addr = sock.accept()
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg

# write in socket
def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent


#readsocks = myreceive(sock=s,msglen=1024)
#writesocks = mysend(sock=s,msg='1024')
while True:
    conn, addr = s.accept()
    readsocks = myreceive(sock=s,msglen=1024)
    writesocks = mysend(sock=s,msg='1024')
    readables, writeables, exceptions = \
    select(readsocks, writesocks, [])
    for sockobj in readables:
        data = sockobj.recv(512)
        if not data:
            sockobj.close()
            readsocks.remove(sockobj)
        if data =='close' or data == 'Close': break
        else:
            print('\tgot', data, 'on', id(sockobj))
