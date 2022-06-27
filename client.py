import socket
import threading
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from encode_decode import *
# encode, decode

client_socket = socket.socket()

window = tk.Tk()
window.title('HDB3 Client')
window.minsize(200, 150)
window.maxsize(200, 150)


def connect():
    try:
        # client_socket.connect((host.get(), int(port.get())))
        connect_frame.lower(belowThis=message_frame)
        message_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        window.minsize(400, 300)
        window.maxsize(400, 300)
    except TimeoutError:
        print("Nao foi possivel conectar a" + host.get() + ":" + port.get())


def check_if_local():
    if local_connection_toggle.get():
        host_entry.configure(state='disabled')
        host.set(socket.gethostname())
    else:
        host_entry.configure(state='normal')
        host.set('')


# inicializa widgets da tela de conexao
connect_frame = tk.Frame(window)
connect_frame.grid(column=0, row=0)

connect_main_label = tk.Label(connect_frame, text="Nova conexao")
connect_main_label.grid(column=0, row=0, sticky=tk.W)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

local_connection_toggle = tk.BooleanVar()
local_connection_checkbox = tk.Checkbutton(connect_frame, text="Conexao local", variable=local_connection_toggle,
                                           command=check_if_local)
local_connection_checkbox.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.S, tk.N))

host_entry_label = tk.Label(connect_frame, text="Host")
host_entry_label.grid(column=0, row=2, sticky=(tk.W, tk.E))

host = tk.StringVar()
host_entry = tk.Entry(connect_frame, width=7, textvariable=host)
host_entry.grid(column=1, row=2, sticky=(tk.W, tk.E, tk.S, tk.N))

port_entry_label = tk.Label(connect_frame, text="Port")
port_entry_label.grid(column=0, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

port = tk.StringVar()
port.set('0000')
port_entry = tk.Entry(connect_frame, width=7, textvariable=port)
port_entry.grid(column=1, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

connect_button = tk.Button(connect_frame, command=connect, text='Conectar')
connect_button.grid(column=1, row=4, sticky=(tk.W, tk.E, tk.S, tk.N))

# #### inicializa widgets da tela de mensagem ####
message_frame = tk.Frame(window)
# message_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))

host_connected_label = tk.Label(message_frame, text=("Host: " + host.get()))
host_connected_label.grid(column=0, row=0, sticky=(tk.W, tk.S, tk.N))

port_connected_label = tk.Label(message_frame, text=("Port: " + port.get()))
port_connected_label.grid(column=0, row=1, sticky=(tk.W, tk.S, tk.N))

# #### lado de envio ####
send_message_label = tk.Label(message_frame, text="Enviar Mensagem")
send_message_label.grid(column=0, row=2, sticky=(tk.W, tk.S, tk.N))

message_out_label = tk.Label(message_frame, text="Mensagem")
message_out_label.grid(column=0, row=3, sticky=(tk.W, tk.S, tk.N))

message_out = tk.StringVar()
message_out_entry = tk.Entry(message_frame, width=10, textvariable=message_out)
message_out_entry.grid(column=0, row=4, sticky=(tk.W, tk.S, tk.N))

binary_out_label = tk.Label(message_frame, text="Binario")
binary_out_label.grid(column=0, row=5, sticky=(tk.W, tk.S, tk.N))

binary_out = tk.StringVar()
binary_out_entry = tk.Entry(message_frame, width=10, textvariable=binary_out, state='readonly')
binary_out_entry.grid(column=0, row=6, sticky=(tk.W, tk.S, tk.N))

algorithm_out_label = tk.Label(message_frame, text="Algoritmo")
algorithm_out_label.grid(column=0, row=7, sticky=(tk.W, tk.S, tk.N))

algorithm_out = tk.StringVar()
algorithm_out_entry = tk.Entry(message_frame, width=10, textvariable=algorithm_out, state='readonly')
algorithm_out_entry.grid(column=0, row=8, sticky=(tk.W, tk.S, tk.N))

send_button = tk.Button(message_frame, text="Enviar")
send_button.grid(column=1, row=4, sticky=(tk.W, tk.S, tk.N))

# #### lado de recebimento ####
recieved_label = tk.Label(message_frame, text="Recebido")
recieved_label.grid(column=3, row=2, sticky=(tk.W, tk.S, tk.N))

algorithm_in_label = tk.Label(message_frame, text="Algoritmo")
algorithm_in_label.grid(column=3, row=3, sticky=(tk.W, tk.S, tk.N))

algorithm_in = tk.StringVar()
algorithm_in_entry = tk.Entry(message_frame, width=10, textvariable=algorithm_in, state='readonly')
algorithm_in_entry.grid(column=3, row=4, sticky=(tk.W, tk.S, tk.N))

binary_in_label = tk.Label(message_frame, text="Binario")
binary_in_label.grid(column=3, row=5, sticky=(tk.W, tk.S, tk.N))

binary_in = tk.StringVar()
binary_in_entry = tk.Entry(message_frame, width=10, textvariable=binary_in, state='readonly')
binary_in_entry.grid(column=3, row=6, sticky=(tk.W, tk.S, tk.N))

message_in_label = tk.Label(message_frame, text="Mensagem")
message_in_label.grid(column=3, row=7, sticky=(tk.W, tk.S, tk.N))

message_in = tk.StringVar()
message_in_entry = tk.Entry(message_frame, width=10, textvariable=message_in, state='readonly')
message_in_entry.grid(column=3, row=8, sticky=(tk.W, tk.S, tk.N))

window.mainloop()

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