import socket
from _thread import start_new_thread

def determine_winner(p1, p2):     #DE MODIFICAT IN FUNCTIE DE CERINTA
    if p1 == p2:
        return "draw"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "player1"
    else:
        return "player2"

def client_thread(conn, player):
    conn.send(player.encode()) #CONEXIUNEA CU CLIENTUL 
    while True:         
        try:
            choice = conn.recv(1024).decode()     
            if not choice or choice == "surrender":  #DE AICI
                break
            choices[player] = choice
            if len(choices) == number_of_clients:
                winner = determine_winner(choices["player1"], choices["player2"])
                for p, c in connections.items():
                    p.send(winner.encode())          #PANA AICI DE MODIFICAT IN FUNCTIE DE CE AI
                choices.clear()            
        except ConnectionResetError:
            break
    print(f"{player} disconnected")
    del connections[player]            
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
number_of_clients=2
server.bind((host, port))
server.listen(number_of_clients)

connections = {}       #DICTIONARELE TREBUIE MODIFICATE
choices = {}           #AICI LA FEL
player_number = 1

while len(connections) < number_of_clients:       #DE AICI 
    conn, addr = server.accept()
    player = f"player{player_number}"
    connections[player] = conn
    print(f"{player} connected")
    start_new_thread(client_thread, (conn, player))
    player_number += 1                          #PANA AICI DE MODIFICAT IN FUNCTIE DE CE AI

while len(connections) > 0:
    pass

server.close()

