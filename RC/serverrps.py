import socket
from _thread import start_new_thread

def determine_winner(p1, p2):
    if p1 == p2:
        return "draw"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "player1"
    else:
        return "player2"

def client_thread(conn, player):
    conn.send(player.encode())
    while True:
        try:
            choice = conn.recv(1024).decode()
            if not choice or choice == "surrender":
                break
            choices[player] = choice
            if len(choices) == 2:
                winner = determine_winner(choices["player1"], choices["player2"])
                for p, c in connections.items():
                    c.send(winner.encode())
                choices.clear()
        except ConnectionResetError:
            break
    print(f"{player} disconnected")
    del connections[player]
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
server.bind((host, port))
server.listen(2)

connections = {}
choices = {}
player_number = 1

while len(connections) < 2:
    conn, addr = server.accept()
    player = f"player{player_number}"
    connections[player] = conn
    print(f"{player} connected")
    start_new_thread(client_thread, (conn, player))
    player_number += 1

while len(connections) > 0:
    pass

server.close()

