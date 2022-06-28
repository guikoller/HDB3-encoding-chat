import tkinter as tk
from client import *


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HDB3 Client')
        self.window.minsize(200, 150)
        self.window.maxsize(200, 150)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.local_connection_toggle = tk.BooleanVar()
        self.host = tk.StringVar()
        self.port = tk.StringVar()

        # instancia o cliente
        self.client = Client()

        # cria frame de conexao
        self.connect_frame = tk.Frame(self.window)
        self.host_entry = tk.Entry(self.connect_frame)

        # cria frame de mensagem
        self.message_frame = tk.Frame(self.window)

        self.init_connection_frame()

        self.window.mainloop()

    def init_connection_frame(self):
        tk.Label(self.connect_frame, text="Conectar").grid(column=0, row=0, sticky=tk.W)

        tk.Checkbutton(self.connect_frame, text="Conexao local", variable=self.local_connection_toggle, command=self.check_if_local)\
            .grid(column=0, row=1, sticky=(tk.W, tk.E, tk.S, tk.N))

        tk.Label(self.connect_frame, text="Host").grid(column=0, row=2, sticky=(tk.W, tk.E))

        self.host_entry.configure(width=7, textvariable=self.host)
        self.host_entry.grid(column=1, row=2, sticky=(tk.W, tk.E, tk.S, tk.N))

        tk.Label(self.connect_frame, text="Port").grid(column=0, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

        tk.Entry(self.connect_frame, width=7, textvariable=self.port).grid(column=1, row=3, sticky=(tk.W, tk.E, tk.S, tk.N))

        tk.Button(self.connect_frame, command=self.connect, text='Conectar').grid(column=1, row=4, sticky=(tk.W, tk.E, tk.S, tk.N))

        self.connect_frame.grid(column=0, row=0)

    def connect(self):
        try:
            self.client.connect()
            self.connect_frame.destroy()
            # self.init_message_frame()

        except TimeoutError:
            print('cu')
            # print("Nao foi possivel conectar a" + self.client.get_host() + ":" + self.client.get_port())

    def check_if_local(self):
        if self.local_connection_toggle.get():
            self.host_entry.configure(state='disabled')
            # self.host.set(self.client.local_host())
        else:
            self.host_entry.configure(state='normal')
            self.host.set('')
