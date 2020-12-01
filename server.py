import socket
from datetime import datetime
import random

def time():
    return  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def name():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return "Amit's Linux Machine" + ip

def rand():
    return str(random.randint(1,10000))

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

(client_socket, client_adress) = server_socket.accept()
print("Client connected")
client_socket.send("You can Choose between 4 commands\nTIME, NAME, RAND or EXIT".encode())

ACTIVE = True
while ACTIVE:    
    command = client_socket.recv(1024).decode()
    if command == "TIME":
        client_socket.send(time().encode())

    elif command == "NAME":
        client_socket.send(name().encode())
    
    elif command == "RAND":
        client_socket.send(rand().encode())
    
    elif command == "EXIT":
        ACTIVE = False

    else:
        client_socket.send("Undefined command, try again".encode())


client_socket.close()
server_socket.close()

