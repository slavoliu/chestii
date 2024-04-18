import socket
import random
import threading

def amesteca_cuvant(cuvant):
    cuvant_amestecat = list(cuvant)
    random.shuffle(cuvant_amestecat)
    return ''.join(cuvant_amestecat)
    
    
def handle_client(client_socket, address):
    cuvinte = ["python", "programare", "socket", "server", "client", "joc", "cuvinte", "retea", "computere", "cod"]
    cuvant_ales = random.choice(cuvinte)
    cuvant_amestecat = amesteca_cuvant(cuvant_ales)
    client_socket.send(cuvant_amestecat.encode('utf-8'))
    while True:
        incercare = client_socket.recv(1024).decode('utf-8')
        if incercare == cuvant_ales:
            client_socket.send("Correct!".encode('utf-8'))
            break
        else:
            client_socket.send("Wrong answer! Try again".encode('utf-8'))
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5052
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print("Server is listening...")
    
    
    client_socket, address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()

start_server()