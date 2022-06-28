import socket
import threading
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from encode_decode import *
# encode, decode


class Client:
    def __init__(self):
        self.client_socket = socket.socket()
        self.host = ''
        self.port = 0000

        self.ascii_message = ''
        self.binary_message = ''
        self.plot_message = ''
        self.encoded_message = ''
        self.text_message = ''

        self.is_connected = False

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def set_message(self, message):
        self.text_message = message
        self.ascii_message = asciiEncode(self.text_message)
        self.binary_message = binaryEncode(self.ascii_message)
        self.plot_message = self.binary_message.copy()
        self.encoded_message = HDB3Encode(self.plot_message)

    def send_message(self):
        self.plot_graph(self.plot_message)
        self.client_socket.send(self.encoded_message[0].encode())

    def receive_message(self,hdb3_code):
        self.encoded_message = hdb3_code
        self.binary_message = HDB3Decode(self.encoded_message[0])
        self.ascii_message = binaryDecode(self.binary_message)
        self.text_message = asciiDecode(self.ascii_message)

    def plot_graph(self,message):
        if plt.fignum_exists(True):
            plt.close()
        plt.rcParams["figure.autolayout"] = True
        plt.title('Enviado')
        index = list(np.arange(len(message)))
        plt.bar(index, message)
        plt.show()


    # TDOD: implementar set e get do host e port e métodos com o código do koller:
    #       - send_message
    #       - receive_message
    #       - plot_graph (?)
    #       - outros que tiver

# inicializa widgets da tela de conexao


# if __name__ == '__main__':
#     # pega as inforções do servidor para conexão
#     host = socket.gethostname()
#     port = input()
#
#     # conecta com o servidor
#     client_socket = socket.socket()
#     client_socket.connect((host, int(port)))
#
#     while True:
#         # pega a mesagem do input e envia ao servidor
#         message = encode(input())
#         client_socket.send(message[0].encode())
#
#         # verifica se existe uma janela de gráfico aberta e fecha se existir
#         if plt.fignum_exists(True):
#             plt.close()
#
#         # plota o gráfico da mensagem codificada
#         plt.rcParams["figure.autolayout"] = True
#         plt.title('Enviado')
#         index = list(np.arange(len(message[1])))
#         plt.bar(index, message[1])
#         plt.show()
#
#         # espera até receber uma mesagem do servidor
#         data = client_socket.recv(1024).decode()
#
#         print('Recebido:')
#         print(data)
#
#         #tranforma string recebida em um vetor para a plotagem
#         bit_array = []
#         plot_data  = list(''.join(data))
#         for bit in plot_data:
#                 if bit == '+':
#                     bit_array.append(1)
#                 elif bit == '-':
#                     bit_array.append(-1)
#                 else:
#                     bit_array.append(0)
#         # verifica se existe uma janela de gráfico aberta e fecha se existir
#         if plt.fignum_exists(True):
#             plt.close()
#
#         # plota o gráfico da mensagem codificada recebida
#         plt.rcParams["figure.autolayout"] = True
#         plt.title('Recebido')
#         index = list(np.arange(len(bit_array)))
#         plt.bar(index, bit_array)
#         plt.show()
#
#         # decoda a mesagem recebida
#         data = decode(data)
#         print(data)
#
#     client_socket.close()