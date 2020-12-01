import socket

my_socket = socket.socket()
my_socket.connect(("192.168.1.244", 8820))
data = my_socket.recv(1024).decode()
print("[SERVER]:    " + data)

while True:
    print("Type Your Next Command Please:")
    command = input()
    my_socket.send(command.encode())
    data = my_socket.recv(1024).decode()
    if command == "EXIT":
        print("Server Disconnected")
        break
    print("[SERVER]:    " + data)

my_socket.close()

