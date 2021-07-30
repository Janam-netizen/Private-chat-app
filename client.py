from os import system, name
import sys
# import sleep to show output for some time period
from time import sleep

import socket

import select

import threading

message_board = {}

host = socket.gethostbyname("")

port = 12343

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((host, port))

name = input("Enter your name")

server.send(str(name).encode())
clients = []


def create_message_board(client_list):
    for client in client_list:
        if client not in message_board:
            message_board[client] = []



def clear():  # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def enter_chat_area(client_name):
    clear()


    for messages in message_board[client_name]:
        print(messages)


    flag = 0
    while True:
        sockets_list = [sys.stdin, server]
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            if socks == server:
                data = server.recv(1024).decode()

                if ":" in data:

                    sender=data[0:data.index(":")]

                    if sender==client_name:
                        print(data)


                    message_board[sender].append(data)



                else:
                    clients = eval(data)
                    create_message_board(clients)
                    # Equate it to global variable.

            else:


                message = input()
                server.send(str(message).encode())
                data="You:" + message
                message_board[client_name].append(data)




                if message == "exit":
                    flag = 1
                    clear()
                    break
        if flag == 1:
            break


def main():
    while True:

        sockets_list = [sys.stdin, server]

        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])


        for socks in read_sockets:
            if socks == server:
                # print mapping of client names and their IPV6  address
                message = socks.recv(2048).decode()
                if ":" in message:
                    sender=message[0:message.index(":")]
                    message_board[sender].append(message)
                else:
                    clients=eval(message)
                    print(clients)
                    print("creating message board.")

                    create_message_board(clients)


                # A "readable" server socket is ready to accept a connection

                # Give the connection a queue for data we want to send
            else:
                client_name = input("")

                server.send(client_name.encode())

                enter_chat_area(client_name)

        clear()
        print("List of clients:"+str(clients))


main()

