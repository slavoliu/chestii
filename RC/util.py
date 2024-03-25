import socket

HOST=''
PORT=4040
MSG_DELIM=b'\0'
RCV_BYTES=4096

def create_listen_socket(host,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    sock.bind((host,port))
    sock.listen(100)
    return sock

def recv_msg(sock):
    data=bytearray()
    msg=''

    while not msg:
        recvd=sock.recv(RCV_BYTES)
        if not recvd:
            raise ConnectionError()
        data=data+recvd

        if MSG_DELIM in recvd:
            msg=data.rstrip(MSG_DELIM)
        
    msg=msg.decode('utf-8')
    return msg

def prep_msg(msg):
    msg+=MSG_DELIM.decode('utf-8')
    return msg.encode('utf-8')

def send_msg(sock, msg):
    data=prep_msg(msg)
    sock.sendall(data)

