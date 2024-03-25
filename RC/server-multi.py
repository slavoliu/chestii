import util
import threading

HOST=util.HOST
PORT=util.PORT

def handle_client(sock, addr):
    while True:
        try:
            msg=util.recv_msg(sock)
            print('{}:{}'.format(addr,msg))
            util.send_msg(sock,msg)
        except (ConnectionError,BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            sock.close()
            break


if __name__ == '__main__':
    listen_sock=util.create_listen_socket(HOST,PORT)
    addr=listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while True:
        client_sock, addr=listen_sock.accept()
        thread=threading.Thread(target=handle_client, args=[client_sock,addr], daemon=True)
        thread.start()
        print('Connection from {}'.format(addr))

