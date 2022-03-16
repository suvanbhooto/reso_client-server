# reso_client-server by Suvan Bhooto

The goal of this project is to create a client-server application and setr up a communication protocol between the two entities.
On the server you have data(images), the client will ask the server to retrieve images.
&nbsp;
----

## How to use the application

### Server side
The server.py should be in the server.
We should change the ip address in the server.py to that of the server.

### Client side
The client.py should be in the client.
We should change the ip address in the client.py to that of the server.

### To run the application 
1. Run the sever.py on the server
2. Then run client.py on the client
3. Both the server and the client will be able to coomunicate
4. The client can then retrieve the images
&nbsp;

----

## The protocol used

**What is user datagram protocol (UDP)** 

User datagram protocol (UDP) operates on top of the Internet Protocol (IP) to transmit datagrams over a network. UDP does not require the source and destination to establish a three-way handshake before transmission takes place. Additionally, there is no need for an end-to-end connection.

Since UDP avoids the overhead associated with connections, error checks and the retransmission of missing data, it’s suitable for real-time or high performance applications that don’t require data verification or correction. If verification is needed, it can be performed at the application layer.

UDP is commonly used for Remote Procedure Call (RPC) applications, although RPC can also run on top of TCP. RPC applications need to be aware they are running on UDP, and must then implement their own reliability mechanisms.
&nbsp;
---

## How to install the project
Clone the repository both on the server and on the server
```
~git clone git@github.com:suvanbhooto/reso_client-server.git
OR
~git clone https://github.com/suvanbhooto/reso_client-server.git
```
&nbsp;

---

## Python libraries to install on server
```python
~sudo apt install python3-numpy
~sudo apt install python3-pip
~sudo pip3 install pillow
```
&nbsp;

---
## How to run the application
First we should run the server.py on the server and then the client.py on client


```
On server :
~ python3 server.py

On client :
~pyhton3 client.py
```
&nbsp;




