import socket

HOST=''
PORT=4040
MSG_DELIM=b'\0'  # Pentru indicarea mesajului de sfarsit
RCV_BYTES=4096   # Cantitatea maxima de date trimise deodata prin socket

def create_listen_socket(host,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crearea socket-ului
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)   #permite socket-ului să folosească o adresă locală care este în starea TIME_WAIT
    sock.bind((host,port)) #leaga socket-ul de un anumit host:port
    sock.listen(100) #Pune socket ul in modul de ascultare si seteaza coada de conexiuni la un anumit numar
    return sock

def recv_msg(sock):
    data=bytearray() #Creaza obiectul data care este un tablou ce contine date de tip octeti
    msg=''

    while not msg:
        recvd=sock.recv(RCV_BYTES) #aici primeste datele de tip bytes de pe socket
        if not recvd:
            raise ConnectionError() #aici ridica o eroare in cazul in care nu o sa functioneze conexiunea
        data=data+recvd

        if MSG_DELIM in recvd:
            msg=data.rstrip(MSG_DELIM) #Elimina delimitatorul de la sfarsitul mesajului
        
    msg=msg.decode('utf-8') #Decodeaza mesajul in formatul respectiv
    return msg

def prep_msg(msg):
    msg+=MSG_DELIM.decode('utf-8') #Adauga delimitatorul dorit de la sfarsitul mesajului decodat
    return msg.encode('utf-8') #returneaza mesajul codat in formatul specificat

def send_msg(sock, msg):
    data=prep_msg(msg) 
    sock.sendall(data)
    #leaga tot ce a facut mai sus

