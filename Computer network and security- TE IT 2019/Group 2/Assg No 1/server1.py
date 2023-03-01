
#!/usr/bin/env python

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool

import pickle
import socket
import sys

#generate the RSA key
blah = randpool.RandomPool()
RSAKey = RSA.generate(1024, blah.get_bytes)

RSAPubKey = RSAKey.publickey()

#listen for a connection
host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." % port

while 1:
  clientsock, clientaddr = s.accept()
  print "got connection from ", clientsock.getpeername()
  #send the public key over
  clientsock.send(pickle.dumps(RSAPubKey))

  rcstring = ''
  while 1:
    buf = clientsock.recv(1024)
    rcstring += buf
    if not len(buf):
      break
  clientsock.close()
  #done with the network stuff, at least for this connection

  #encmessage is the cipher text
  encmessage = pickle.loads(rcstring)

  print RSAKey.decrypt(encmessage)
  
