# Private-chat-app

## Project Description:

A  command line based chat app that enables users to chat with  other clients privately.

## Project structure:

This repository consists of two files named ```Server.py``` and ```client.py```. 


## Project design

Project  implementation:

The server.py enables us to host the server at a particular port on the  machine running it.

The responsibilities of the server are:
<ol>
<li>Accepting connections from clients

<li>Storing thr list of clients and  continously update the list when a new client joins


<li>Broadcasting the list of clients to other clients

<li>Maintaining the states of client.ie the client could be engaged conversing or choosing the client to chat with.

<li>interpreting messages sent by  clients and responding accordingly.
ie when a client chooses to chat with another client privatelh the server senf every message that the client to the other client
</ol>
Responsibilities of a client inteface are:
<ol>
<li>displaying the list of   online users when the server sends it

<li>Storing and displaying the conversation history

</ol>

## Exectution

To host the server 

```python3 Server.py```

To connect to the server and seeing th client interface:


```python3 client.py ```







