from email import message
from http import client
import threading
from socket import socket

name = input('Please Enter your Name : ')
client = socket()
port = int(input('Enter the port server Running on : '))
client.connect(('localhost', port))

def receiveMessage():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(f'{name}'.encode())
            else:
                print(message)
        except:
            print('Error, Please Reconnect !')
            client.close()
            break

def sendMessage():
    while True:
        message = '{} : {}'.format(name, input(''))
        client.send(message.encode())

threading.Thread(target=receiveMessage).start()
threading.Thread(target=sendMessage).start()