##NAMA  = PUTRI SIWI UTAMI
##KELAS = D
##NIM   = L200180146
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
berkas.write("Brebes\n")
berkas.write("02-01-2001 \n")
berkas.close()

import shelve
f = open("L200180146","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
Tl = f.readline()
f.close()

f = shelve.open("Putri")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

f = shelve.open("Putri")

print f['b'][0]
print f['b'][1]
print f['b'][2]
print f['b'][3]

##Kegiatan 3 praktikum 9
import shelve
f = open("L200180146","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
Tl = f.readline()
f.close()


f = shelve.open("Putri")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

##Kegiatan 4 praktikum 9
import shelve
f = shelve.open("Putri")
print 'Nama :' , f['b'][0]
print 'Asal :' , f['b'][1]
print 'Tl   :' , f['b'][2]
print 'Nim  :' , f['b'][3]
