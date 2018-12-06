import socket
def alas_tinggi(a=0,t=0):
    return (a*t)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter")!= -1:
            param,value= data.split("=")
            if param == "parameter alas":
                a=float(value)
                b=value
                komm.send("parameter dicatat")
            elif param == "parameter tinggi":
                t=float(value)
                c=value
                komm.send("parameter dicatat")
        elif data=='hitung':
            komm.send('luas jajar genjang dengan alas {} tinggi {} adalah {}'.format (b,c,alas_tinggi(a,t)))
        else:
            komm.send('tidak ada')
