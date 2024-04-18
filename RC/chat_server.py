import socket

HOST='127.0.0.1'
PORT=4040
MSG_DELIM=b'\0'
RCV_BYTES=4096

def create_listen_socket(host,port,number_of_connections):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((host,port))
    sock.listen(number_of_connections)
    return sock

def recv_msg(sock):
    data=bytearray()
    msg=''

    while not msg:
        msg_received=sock.recv(RCV_BYTES)
        if not msg_received:
            raise ConnectionError()
        data=data+msg_received

        if MSG_DELIM in msg_received:
            msg=data.rstrip(MSG_DELIM)
        
    msg=msg.decode('utf-8')
    return msg

def prep_msg(msg):
    msg+=MSG_DELIM.decode('utf-8')
    return msg.encode('utf-8')

def send_msg(sock,msg):
    data=prep_msg(msg)
    sock.sendall(data)


def handle_client(sock,addr):
    while True:
        msg=recv_msg(sock)
        try:
            if(msg=='stop'):
                break
            else:
                print(f'Mesajul este {msg}')
                send_msg(sock,msg)
        except(ConnectionError,BrokenPipeError):
            print(f'Closed connection to {addr}')
            sock.close()
            break

if __name__ =="__main__":
    listen_sock=create_listen_socket(HOST,PORT,2)
    addr=listen_sock.getsockname()
    print(f"Server is running on {addr}")

    while True:
        client_sock,addr=listen_sock.accept()
        print(f"Connection from {addr}")
        handle_client(client_sock,addr)  
        






