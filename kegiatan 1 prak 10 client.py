# nama berkas: p_tcpser.py
# TCP Server untuk client p_tcpc.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = {'nama' : 'Putri Siwi Utami',
         'NIM' : 'L200180146'}
while data.lower() != 'keluar' :
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print 'Perintah:' , data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')





















        
        
