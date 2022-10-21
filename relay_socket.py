# python3 .\Desktop\python_tests\relay_socket.py

import socket
import os

 
localIP     = "192.168.75.225"
localPort   = 6038
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
#bytesToSend         = str.encode(msgFromServer)

usv_data = 0
print_data = 0

epoch = 0

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

 
# Listen for incoming datagrams
while(True):

    epoch = epoch + 1

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = ('192.168.75.225',3000)
    #print(address)
    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    #print(clientMsg)
    #print(clientIP)

    # ------------------ Data manipulation ------------------
    usv_data = int(message[2:5])
    print_data = usv_data * 2 

    # ---------------- Log data to file ----------------
    with open(r"C:\Users\admin\Desktop\python_tests\motor_data.txt", 'a') as log_file:
        log_file.write('{}. '.format(epoch))
        log_file.write('Motor 1 = {}'.format(print_data))
        log_file.write("\n")
        print(print_data)

    # Sending a reply to client
    UDPServerSocket.sendto(message, address)