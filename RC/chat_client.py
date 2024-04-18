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



if __name__=="__main__":
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((HOST,PORT))
    except ConnectionError:
        print("Error for connection to socket")

    print("Type message, enter to send, type 'stop' to quit")
        
    while True:
        msg=input()
        if not msg:
            continue

        if msg=="stop": break
        try:
            send_msg(sock,msg)
            print('Sent message: {}'.format(msg))
            msg=recv_msg(sock)
            print('Message was received')

        except ConnectionError:
            print("Socket error during communication")
            sock.close()
            print("Closed connection to server")
            break

    print("Closing connection")
    sock.close() 