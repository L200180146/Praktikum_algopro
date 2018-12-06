#Kegiatan 2. Informasi tentang server

import socket
import platform
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("", 50009))
s.listen (5)
print "Program komunikasi tentang diri anda"
baba = ''
masukan = {'machine' : platform.machine(),
         'release' : platform.release(),
         'system' : platform.system(),
         'version' : platform.version(),
         'node'    : platform.node(),
         'quit' : ' Siapp !!!' }
while baba.lower() != 'quit' :
    komm, addr = s.accept()
    while baba.lower () != 'quit' :
        baba = komm.recv(1024)
        if baba.lower() == 'quit' :
            s.close()
            break
        print 'Command: ', baba
        if masukan.has_key(baba) :
            komm.send(masukan[baba])
        else :
            komm.send('unknown command')












        
        
