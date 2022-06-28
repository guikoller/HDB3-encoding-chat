import tkinter as tk
from client import *


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HDB3 Client')
        self.window.minsize(200, 150)
        self.window.maxsize(200, 150)

        # instancia o cliente
        self.client = Client()

        # widgets do frame de conexao
        self.connect_frame = tk.Frame(self.window)
        self.connect_frame.grid(column=0, row=0)

        self.connect_main_label = tk.Label(self.connect_frame, text="Nova conexao")
        self.connect_main_label.grid(column=0, row=0, sticky=tk.W)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.local_connection_toggle = tk.BooleanVar()
        self.local_connection_checkbox = tk.Checkbutton(self.connect_frame, text="Conexao local",
                                                   variable=self.local_connection_toggle,
                                                   command=self.check_if_local)
        self.local_connection_checkbox.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.host_entry_label = tk.Label(self.connect_frame, text="Host")
        self.host_entry_label.grid(column=0, row=2, sticky=(tk.W, tk.E))

        self.host = self.tk.StringVar()
        self.host_entry = tk.Entry(self.connect_frame, width=7, textvariable=self.host)
        self.host_entry.grid(column=1, row=2, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.port_entry_label = tk.Label(self.connect_frame, text="Port")
        self.port_entry_label.grid(column=0, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.port = tk.StringVar()
        self.port.set('0000')
        self.port_entry = tk.Entry(self.connect_frame, width=7, textvariable=self.port)
        self.port_entry.grid(column=1, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.connect_button = tk.Button(self.connect_frame, command=self.connect, text='Conectar')
        self.connect_button.grid(column=1, row=4, sticky=(tk.W, tk.E, tk.S, tk.N))

        # #### inicializa widgets da tela de mensagem ####
        self.message_frame = tk.Frame(self.window)
        # message_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.host_connected_label = tk.Label(self.message_frame, text=("Host: " + self.host.get()))
        self.host_connected_label.grid(column=0, row=0, sticky=(tk.W, tk.S, tk.N))

        self.port_connected_label = tk.Label(self.message_frame, text=("Port: " + self.port.get()))
        self.port_connected_label.grid(column=0, row=1, sticky=(tk.W, tk.S, tk.N))

        # #### lado de envio ####
        self.send_message_label = tk.Label(self.message_frame, text="Enviar Mensagem")
        self.send_message_label.grid(column=0, row=2, sticky=(tk.W, tk.S, tk.N))

        self.message_out_label = tk.Label(self.message_frame, text="Mensagem")
        self.message_out_label.grid(column=0, row=3, sticky=(tk.W, tk.S, tk.N))

        self.message_out = tk.StringVar()
        self.message_out_entry = tk.Entry(self.message_frame, width=10, textvariable=self.message_out)
        self.message_out_entry.grid(column=0, row=4, sticky=(tk.W, tk.S, tk.N))

        self.binary_out_label = tk.Label(self.message_frame, text="Binario")
        self.binary_out_label.grid(column=0, row=5, sticky=(tk.W, tk.S, tk.N))

        self.binary_out = tk.StringVar()
        self.binary_out_entry = tk.Entry(self.message_frame, width=10, textvariable=self.binary_out, state='readonly')
        self.binary_out_entry.grid(column=0, row=6, sticky=(tk.W, tk.S, tk.N))

        self.algorithm_out_label = tk.Label(self.message_frame, text="Algoritmo")
        self.algorithm_out_label.grid(column=0, row=7, sticky=(tk.W, tk.S, tk.N))

        self.algorithm_out = tk.StringVar()
        self.algorithm_out_entry = tk.Entry(self.message_frame, width=10, textvariable=self.algorithm_out, state='readonly')
        self.algorithm_out_entry.grid(column=0, row=8, sticky=(tk.W, tk.S, tk.N))

        self.send_button = tk.Button(self.message_frame, text="Enviar")
        self.send_button.grid(column=1, row=4, sticky=(tk.W, tk.S, tk.N))

        # #### lado de recebimento ####
        self.recieved_label = tk.Label(self.message_frame, text="Recebido")
        self.recieved_label.grid(column=3, row=2, sticky=(tk.W, tk.S, tk.N))

        self.algorithm_in_label = tk.Label(self.message_frame, text="Algoritmo")
        self.algorithm_in_label.grid(column=3, row=3, sticky=(tk.W, tk.S, tk.N))

        self.algorithm_in = tk.StringVar()
        self.algorithm_in_entry = tk.Entry(self.message_frame, width=10, textvariable=self.algorithm_in, state='readonly')
        self.algorithm_in_entry.grid(column=3, row=4, sticky=(tk.W, tk.S, tk.N))

        self.binary_in_label = tk.Label(self.message_frame, text="Binario")
        self.binary_in_label.grid(column=3, row=5, sticky=(tk.W, tk.S, tk.N))

        self.binary_in = tk.StringVar()
        self.binary_in_entry = tk.Entry(self.message_frame, width=10, textvariable=self.binary_in, state='readonly')
        self.binary_in_entry.grid(column=3, row=6, sticky=(tk.W, tk.S, tk.N))

        self.message_in_label = tk.Label(self.message_frame, text="Mensagem")
        self.message_in_label.grid(column=3, row=7, sticky=(tk.W, tk.S, tk.N))

        self.message_in = tk.StringVar()
        self.message_in_entry = tk.Entry(self.message_frame, width=10, textvariable=self.message_in, state='readonly')
        self.message_in_entry.grid(column=3, row=8, sticky=(tk.W, tk.S, tk.N))


    def connect(self,host, port):
        try:
            self.client.connect()
            self.connect_frame.lower(belowThis=self.message_frame)
            self.message_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))
            self.window.minsize(400, 300)
            self.window.maxsize(400, 300)
            self.is_connected = True
        except TimeoutError:
            print("Nao foi possivel conectar a" + self.client.get_host() + ":" + self.client.get_port())


    def check_if_local(self):
        if self.local_connection_toggle.get():
            self.host_entry.configure(state='disabled')
            self.host.set(self.client.local_host())
        else:
            self.host_entry.configure(state='normal')
            self.host.set('')
