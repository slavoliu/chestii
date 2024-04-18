import socket

host = '127.0.0.1'
port = 5052

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Try guessing")
data = client_socket.recv(1024).decode('utf-8')
print(data)

while True:
    guess = input("Enter your answer:")
    client_socket.send(guess.encode('utf-8'))
    answer = client_socket.recv(1024).decode('utf-8')
    
    print(answer)
    
    if answer.startswith("Correct!"):
        break
        
client_socket.close()