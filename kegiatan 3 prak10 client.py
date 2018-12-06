import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50006))
print "menghitung luas jajar genjang"
while pesan != 'keluar':
    pesan = raw_input('pesan :  ')
    s.send(pesan)
    if pesan.lower()=='keluar':
        response = s.recv(1024)
        print 'respon: -'
        s.close()
        break
    elif pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'respon:', response
s.close()
 
