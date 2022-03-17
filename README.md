# reso_client-server by Suvan Bhooto

The goal of this project is to create a client-server application and set up a communication protocol between the two entities.
On the server you have data(images), the client will ask the server to retrieve images.
&nbsp;

----

## How to use the application

### Server side
The server.py should be in the server.
We should change the ip address in the server.py to that of the server.
The images should be on the server.

### Client side
The client.py should be in the client.


### To run the application 
1. Run the sever.py on the server
2. Enter the port you want to use(eg: 5005)
3. Then run client.py on the client
4. Enter the display the ip address display on the server
5. Both the server and the client will be able to coomunicate
6. The client must then insert the name of the image he wants to download(eg: image.png)
&nbsp;



On server
```
10.27.0.41
Enter desired port --> 5005
Running on IP: 10.27.0.41
Running on port: 5005
```

On client
```
<__main__.Client object at 0x7fc6c5d26dc0>
Enter ip --> 10.27.0.41
Enter port --> 5005
Enter file name on server --> img.jpg
img.jpg successfully downloaded.

```

----

## The protocol used

 
**What is TCP?**

TCP stands for Transmission Control Protocol a communications standard that enables application programs and computing devices to exchange messages over a network. It is designed to send packets across the internet and ensure the successful delivery of data and messages over networks.

TCP is one of the basic standards that define the rules of the internet and is included within the standards defined by the Internet Engineering Task Force (IETF). It is one of the most commonly used protocols within digital network communications and ensures end-to-end data delivery.

TCP organizes data so that it can be transmitted between a server and a client. It guarantees the integrity of the data being communicated over a network. Before it transmits data, TCP establishes a connection between a source and its destination, which it ensures remains live until communication begins. It then breaks large amounts of data into smaller packets, while ensuring data integrity is in place throughout the process.

As a result, high-level protocols that need to transmit data all use TCP Protocol.  Examples include peer-to-peer sharing methods like File Transfer Protocol (FTP), Secure Shell (SSH), and Telnet. It is also used to send and receive email through Internet Message Access Protocol (IMAP), Post Office Protocol (POP), and Simple Mail Transfer Protocol (SMTP), and for web access through the Hypertext Transfer Protocol (HTTP).

An alternative to TCP is the User Datagram Protocol (UDP), which is used to establish low-latency connections between applications and decrease transmissions time. TCP can be an expensive network tool as it includes absent or corrupted packets and protects data delivery with controls like acknowledgments, connection startup, and flow control. 

UDP does not provide error connection or packet sequencing nor does it signal a destination before it delivers data, which makes it less reliable but less expensive. As such, it is a good option for time-sensitive situations, such as Domain Name System (DNS) lookup, Voice over Internet Protocol (VoIP), and streaming media.


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





