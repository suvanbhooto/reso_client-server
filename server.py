import socket
import numpy as np
from PIL import Image

img_data = Image.open('img.jpg')
img_arr = np.array(img_data)



z =  len(img_arr)


for i in img_arr.shape[1::-1]: # img.shape -> (width,height,channel)

    if(i%2 == 0):

    	msgFromServer= "pair"

	


    else:

        msgFromServer= "impair"




 

localIP     = "10.27.0.41"

localPort   = 12345

bufferSize  = 1024

 

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)
