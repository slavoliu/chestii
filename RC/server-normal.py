import util

HOST= util.HOST
PORT=util.PORT

def handle_client(sock, addr):
    while True:
        try:
            msg=util.recv_msg(sock)
            print('{}: {}'.format(addr,msg))
            util.send_msg(sock,msg)

        except (ConnectionError, BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            sock.close()
            break


if __name__ == '__main__':
    listen_sock=util.create_listen_socket(HOST,PORT)
    addr= listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while True:
        client_sock,addr=listen_sock.accept()
        print('Connection from {}'.format(addr))
        handle_client(client_sock,addr)
