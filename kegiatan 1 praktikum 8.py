a = {'NIM':'L200180146','Nama':'Putri Siwi Utami','Alamat':'jalan duwet','Prodi':'informatika','Fakultas':'FKI','Zodiak':'Capricorn','Panggilan':'Siwi'}

print "Pilihan yang tersedia:"
print "N menampilkan Nama"
print "n menampilkan NIM"
print "A menampilkan Alamat"
print "P menampikan Prodi"
print "f menampilkan Fakultas"
print "z menampilkan Zodiak"
print "o menampilkan Panggilan"


def Nama():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Nama:' + a['Nama']


def NIM():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'NIM:' + a['NIM']

def Alamat():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Alamat:' + a['Alamat']

def Prodi():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Prodi:' + a['Prodi']

def Fakultas():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Fakultas:' + a['Fakultas']


def Zodiak():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Zodiak:' + a['Zodiak']


def Panggilan():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Panggilan:' + a['Panggilan']


repeat = True

while repeat :
    x = raw_input("Pilihan Saudara :")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM()
    elif x == "A" :
        Alamat()
    elif x == "P" :
        Prodi()
    elif x == "f" :
        Fakultas()
    elif x == "z" :
        Zodiak()
    elif x == "o" :
        Panggilan()
        
