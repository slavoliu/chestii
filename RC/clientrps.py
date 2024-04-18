import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    client.connect((host, port))
    player = client.recv(1024).decode()
    print(f"You are {player}")

    while True:
        choice = input("Enter your choice (rock, paper, scissors) or 'surrender' to quit: ").lower()
        client.send(choice.encode())
        if choice == "surrender":
            break
        result = client.recv(1024).decode()
        if result == player:
            print("You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")
    
    print("Game over.")
    client.close()

if __name__ == "__main__":
    main()

