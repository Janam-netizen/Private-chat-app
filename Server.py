import socket

import threading


class Network:
    def __init__(self):
        self.client_list = []  # To store the client socket objects
        self.client_names = []
        self.client_states = {}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname("")
        self.port = 12343
        self.addr = (self.server, self.port)
        self.socket.bind(self.addr)
        self.socket.listen(100)

    def start(self):

        while True:
            conn, addr = self.socket.accept()
            """
            Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
            the IP address of the client that just connected
            """

            self.client_list.append(conn)
            client_name = conn.recv(2048)
            print(str(addr)+" joined.")
            self.client_names.append(client_name.decode())
            self.client_states[conn] = "M"

            # maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
            # Prints the address of the person who just connected
            threading._start_new_thread(self.clienthread, (conn,))
            # creates and individual thread for every user that connects

    def clienthread(self, conn):
        self.display_online_users()
        while True:

            message=conn.recv(2048)

            if self.client_states[conn]=="M":
                self.client_states[conn]=self.client_list[self.client_names.index(message.decode())]
            else:


                data = self.client_names[self.client_list.index(conn)]+":"+message.decode()
                print("sending " +data)
                self.client_states[conn].send(data.encode())

                if message.decode()=="exit":
                    self.client_states[conn]="M"






    def display_online_users(self,):

        # Convert To String
        temp = str(self.client_names)

        # Encode String
        temp=str(temp).encode()

        # Send Encoded String version of the List
        for conn in self.client_list:

                conn.send(temp)


n = Network()

n.start()
