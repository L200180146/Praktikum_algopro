##NAMA  = PUTRI SIWI UTAMI
##NIM   = L200180146
##KELAS = D

##Kegiatan 1 praktikum 9
berkas = open("L200180146","w")
berkas.write("L200180146 \n")
berkas.write("02-01-2001 \n")
berkas.write("Putri Siwi Utami \n")
berkas.close()

##Kegiatan 2 praktikum 9
berkas = open("L200180146","w")
berkas.write("L200180146 \n")
berkas.write("Putri Siwi Utami \n")
berkas.write("Brebes \n")
berkas.write("02-01-2001 \n")
berkas.close()

import shelve
f = open("L200180146","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
TL = f.readline()
f.close()

f = shelve.open("Siwi")
f['a'] = [Nama, Asal, TL, Nim]
f.close()

f = shelve.open("Siwi")

print f['a'][0]
print f['a'][1]
print f['a'][2]
print f['a'][3]

##Kegiatan 3 praktikum 9
import shelve
f = open("L200180146","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
TL = f.readline()
f.close()


f = shelve.open("Siwi")
f['a'] = [Nama, Asal, TL, Nim]
f.close()

##Kegiatan 4 praktikum 9
import shelve
f = shelve.open("Siwi")
print 'Nama :' , f['a'][0]
print 'Asal :' , f['a'][1]
print 'TL   :' , f['a'][2]
print 'Nim  :' , f['a'][3]
