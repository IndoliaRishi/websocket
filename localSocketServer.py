import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
print(f"socket server url {socket.gethostname()}")
s.bind((socket.gethostname(),1234))
s.listen(5)

while True: 
      clientsocket, address = s.accept()
      print(f"Connection from {address} has been established!")
      clientsocket.send(bytes("Welcome to server", "utf-8"))