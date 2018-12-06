#Kegiatan 2. Informasi data diri(client)

import socket
import platform
hostname = 'localhost'
client = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50009))
print "Program komunikasi tentang diri anda "
while client.lower() != 'quit' :
    client = raw_input( 'Command: ')
    s.send(client)
    if client.lower() != 'quit' :
        response = s.recv(1024)
        print "jawab: " , response
s.close()
