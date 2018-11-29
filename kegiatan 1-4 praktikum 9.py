##NAMA  =PUTRI SIWI UTAMI
##NIM   =L200180146
##KELAS =D

##Kegiatan 1 praktikum 9 (menulis berkas teks)
berkas = open("L200180146","w")
berkas.write("L200180146 \n")
berkas.write("02-01-2001 \n")
berkas.write("Putri Siwi Utami \n")
berkas.close()

##Kegiatan 2 praktikum 9 (membaca berkas teks)
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
Tl = f.readline()
f.close()

f = shelve.open("siwi")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

f = shelve.open("siwi")

print f['b'][0]
print f['b'][1]
print f['b'][2]
print f['b'][3]

##Kegiatan 3 praktikum 9(membaca data dari berkas teks dan menyimpan ke shelve)
import shelve
f = open("L200180146","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
Tl = f.readline()
f.close()


f = shelve.open("siwi")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

##Kegiatan 4 praktikum 9 (membaca shelve)
import shelve
f = shelve.open("siwi")
print 'Nama :' , f['b'][0]
print 'Asal :' , f['b'][1]
print 'Tl   :' , f['b'][2]
print 'Nim  :' , f['b'][3]
