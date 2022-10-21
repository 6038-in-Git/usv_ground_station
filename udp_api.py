# cd .\Desktop\python_tests
# uvicorn udp_api:get_usv_udp --reload

import requests
import json
import time
import socket
from fastapi import FastAPI

# ------------------------------ Initialization ------------------------------
# ------- UDP Socket -------
localIP     = "192.168.75.225"
localPort   = 3000
bufferSize  = 1024
message = b"000000"

# ------- Variables -------
usv_data = 0
print_data = 0

# ------- API -------
get_usv_udp = FastAPI()


# ------------------ Create a datagram socket ------------------

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")


# ------------------ UPDATE UDP ------------------
def update_udp():
	# ------------------ Receive datagram ------------------
	_message = b"000000"
	_usv_data = 0
	for x in range(10):
		_bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	_message = _bytesAddressPair[0]
	_address = _bytesAddressPair[1]
	#clientMsg = "Message from Client:{}".format(message)
	#clientIP  = "Client IP Address:{}".format(address)

	# ------------------ Data manipulation ------------------
	_usv_data = int(_message[2:5])
	_print_data = _usv_data * 2 

	# Sending a reply to client
	#msgFromServer = 'Hello UDP Client, Motor: {}'.format(_print_data)
	#bytesToSend   = str.encode(msgFromServer)
	#UDPServerSocket.sendto(bytesToSend, _address)
	
	return _print_data


# ----------------------------- Paths Operations -----------------------------
@get_usv_udp.get("/")
async def root():
	return {"message": "Hello World"}

@get_usv_udp.get("/get_data/motor")
async def read_motor():
	print_data = update_udp()
	print(print_data)
	return {print_data}



