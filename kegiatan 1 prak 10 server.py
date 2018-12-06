# nama berkas: p_tcpcli.py
# Client TCP  untuk server p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "Program komunikasi tentang diri anda"
while pesan.lower() != 'keluar':
    pesan = raw_input('Perintah: ')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Jawab:',response
    else :
        print "siap!!!"
s.close()
