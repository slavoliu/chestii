import sys, socket
import util

HOST=sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT=util.PORT

if __name__ == '__main__':
    try:
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((HOST,PORT))
        print("here")
    except ConnectionError:
        print('Socket error on connection')
        sys.exit(1)

    print('\nConnected to {}:{}'.format(HOST,PORT))
    print("Type message, enter to send, 'q' to quit")

    while True:
        msg = input()
        if not msg:
            continue
        
        if msg == 'q': break
        try:
            util.send_msg(sock,msg)
            print('Sent message: {}'.format(msg))
            msg=util.recv_msg(sock)
            print('Received echo: '  +msg)

        except ConnectionError:
            print("Socket error during communication")
            sock.close()
            print("Closed connection to server")
            break

    print("Closing connection")
    sock.close()    

