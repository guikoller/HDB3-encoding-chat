import tkinter as tk
from client import *


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HDB3 Client')
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.geometry('400x300')

        self.local_connection_toggle = tk.BooleanVar()
        self.host = tk.StringVar()
        self.port = tk.StringVar()

        # instancia o cliente
        self.client = Client()

        # cria frame de conexao e widgets
        self.connect_frame = tk.Frame(self.window)
        self.host_entry = tk.Entry(self.connect_frame)

        # cria frame de mensagem e widgets
        self.message_frame = tk.Frame(self.window)
        self.history_text = tk.Text(self.message_frame)
        self.message_text = tk.Text(self.message_frame)

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

        self.connect_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))

    def init_message_frame(self):
        self.history_text.config(height=20, width=100, state='disabled')
        self.history_text.grid(column=0, row=0, columnspan=2, sticky=tk.W)

        self.message_text.config(height=5, width=80)
        self.message_text.grid(column=0, row=1, sticky=tk.W)

        send_button = tk.Button(self.message_frame, command=self.send_message, height=2, width=20, text='Enviar')
        send_button.grid(column=1, row=1, sticky=tk.W)

        self.message_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N), padx=5, pady=5)

    def connect(self):
        try:
            self.client.host = self.host.get()
            self.client.port = int(self.port.get())
            self.client.connect()
            self.connect_frame.destroy()
            self.init_message_frame()

        except TimeoutError:
            print("Nao foi possivel conectar a" + self.client.host + ":" + self.client.port)

    def check_if_local(self):
        if self.local_connection_toggle.get():
            self.host_entry.configure(state='disabled')
            self.host.set(socket.gethostname())
        else:
            self.host_entry.configure(state='normal')
            self.host.set('')

    def send_message(self):
        message = self.message_text.get('0.0', tk.END)
        self.client.set_message_to_send(message)

        self.client.send_message()
        self.receive_message()

    def receive_message(self):
        self.client.receive_message()