from socket import socket
import threading

server = socket()

while True:
    port = int(input("Enter the port Number : "))
    try:
        server.bind(('localhost', port))
        break
    except:
        print('The port is already taken, Please try another port !')

server.listen()

clients = []
namesDict = dict()

# Braodcast a Message to all the clinets
def broadCast(message):
    for client in clients:
        client.send(message)

# To handle each client
def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            broadCast(message)
        except:
            clients.remove(client)
            name = namesDict[client]
            del namesDict[client]
            client.close()
            broadCast(f'{name} : Left the Room !')
            break

while True:
    # Accepting a connection
    client, address = server.accept()
    print(f'Connected with {str(address)}')

    # Taking info about the client
    client.send('NICK'.encode())
    name = client.recv(1024).decode()
    clients.append(client)
    namesDict[client] = name

    # Broadcasting to all clients that new client joined
    broadCast(f'{name} : Joined the Room !'.encode())
    client.send('Connected!'.encode())

    threading.Thread(target=handleClient, args=(client,)).start()