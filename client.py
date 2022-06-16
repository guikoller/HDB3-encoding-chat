from email import message
from http import client
import threading
from socket import socket
import tkinter as tk
from encode_decode import encode, decode

from numpy import *

#window = tk.Tk()
#window.title('CHAT')
#window.geometry('400x300')

name = input('Please Enter your Name : ')
client = socket()
port = int(input('Enter the port server Running on : '))
client.connect(('localhost', port))

#window.mainloop

def receiveMessage():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(f'{name}'.encode())
            else:
                if '+' and '-' in message:
                    message = decode(message)
                
                print(message)
        except:
            print('Error, Please Reconnect !')
            client.close()
            break

def sendMessage():
    while True:
        message = '{} : {}'.format(name, input(''))
        message = encode(message)
        client.send(message.encode())

threading.Thread(target=receiveMessage).start()
threading.Thread(target=sendMessage).start()
