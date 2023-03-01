#!/usr/bin/env python

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool

import pickle
import socket

host = 'localhost'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

#this should loop around until a delimeter is read
#or something similar
rcstring = s.recv(2048)

#this object is of type RSAobj_c, which only has public key
#encryption is possible, but not decryption
publickey = pickle.loads(rcstring)

print publickey

#encrypt the top secret data
secretText = publickey.encrypt("Hello, this is Ratan.", 32)

s.sendall(pickle.dumps(secretText))
s.close()

