Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> ##PRAKTIKUM 6 KEGIATAN 1
>>> nama
'putri'
>>> nim
'L200180146'
>>> nama_lengkap
'putri siwi utami'
>>> alamat
'jalan duwet 12'
>>> tempat_tanggal_lahir
'brebes, 2 januari 2001'
>>> prodi
'informstika'
>>> fakultas
'FKI'
>>> zodiak
'capricorn'
>>> hobi
'menggambar'
>>> bias
'park chanyeol'
>>> ================================ RESTART ================================
>>> ##PRAKTKUM 6 KEGIATAN 2
>>> NamaSingkat
'P. S. Utami'
>>> password
'Put146'
>>> 

>>> nama = 'putri siwi utami'
>>> nim = 'L200180146'
>>> x = '1' + nim [7:]
>>> a = int(x)
>>> b = len (nama)
>>> type (a)
<type 'int'>
>>> type (b)
<type 'int'>
>>> a/b
71
>>> a
1146
>>> b
16
>>> a//b
71
>>> a/ / b
SyntaxError: invalid syntax
>>> b**2
256
>>> a%b
10
>>> c = 12.5
>>> type (c)
<type 'float'>
>>> a / c
91.68
>>> a / / c
SyntaxError: invalid syntax
>>> a//c
91.0
>>> a%c
8.5
>>> 
>>> c>b
False
>>> type (c>b)
<type 'bool'>
>>> a>b and b>c
True
>>> a>1100 or b<10
True
>>>##PRAKTIKUM 6 KEGIATAN 2
>>> nama='putri siwi utami'
>>> nim='L200180146'
>>> x='1' + nim[7:]
>>> #didalam string, digunakan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh
>>> #dari variable nim sampai selesai.
>>> print (x) #menampilkan variable x
1146
>>> a = int (x) #menampilkan string ke integer
>>> print (a) #menampilkan variable a
1146
>>> b = len(nama) #konversi string dalam variable nama kedalam angka
>>> print (b) #menampilkan variable b
16
>>> type (a) #menampilkan type data dari variable a
<type 'int'>
>>> type (b) #menampilkan type data dari variable b
<type 'int'>
>>> a/b
>>> #operasi pembagian antara bilangan dari variable a dengan b. type data yang bisa untuk
>>> #membagi bilangan hanya bila data tersebut bertype integer/float
71
>>> a//b
>>> #operasi pembagian antar bilangan dengan pembulatan ke bawah.type data yang bisa
>>> #untuk membagi bilangan hanya bila data bertype integer/float
71
>>> 10*(a-999) #operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer maupun float
1470
>>> b**2 #operasi ini digunakan untuk perpangkatan,type yang digunakan untuk operasi ini yaitu integer dan float
256
>>> a%b #operasi ini digunakan untuk memunculkan sisa hasil bagi
10
>>> c=12.5 #variable c berups angka yang terdapat koma berarti type data pada variable c yaitu float
>>> type (c) #menampilkan type data dari variable c
<type 'float'>
>>> a/c
>>> #operasi pembagian antara bilangan dari variable a dengan c. type data yang bisa untuk membagi
>>> #bilangan hanya bila data bertype integer/float
91.68
>>> a//c
>>> #operasi pembagian anat bilangan dengan pembulatan kebawah. type data yang bisa membagi
>>> #bilangan hanya bila data bertype integer/float
91.0
>>> a%c #operasi ini digunakan untuk memunculkan sisa hasil bagi.
8.5
>>> c>b #operasi ini digunakan untuk menampilkan perbandingan lebih dari. type data ini adalah boolean.
False
>>> type (c > b) #menampilkan type data dari (c > b)
<type 'bool'>
>>> a > b and b > c
>>> #pada data terdapat dua pernyataan 1146 > 16 dan 16 > 12.5. karena kedua pernyataan tersebut
>>> #dihubungkan dengan operator logika "and"maka akan menghasilkan dua kemungkinan nilai, yaitu true atau false
True
>>> a > 1100 or b < 10
>>> #operasi logika yang digunakan pada data adalah "or" apabila salah satu dari pernyataan
>>> #benar akan menghasilkan nilai benar . dari pernyataan disamping diartikan 1146 > 1100 atau 16 < 10 . dengan
>>> #1146 > 1100 maka pernyataan ini benar sedangkan pernyataan ini 16 < 10 salah  maka nilai yang akan didapat adalah benar  
True
>>> ##PRAKTIKUM 6 KEGIATAN 4
>>> Nama = 'Putri Siwi Utami'
>>> NIM = 146
>>> Tinggi = 1.54
>>> Berat = 63
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama) #Sebuah Tuple
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama] #Sebuah list
>>> type (Aku)#Menampilkan type data variable aku
<type 'tuple'>
>>> Aku [0]# menampilkan eleman tuple indeks 0
2001
>>> a = NIM % 4; Aku[a]# NIM 146 dibagi 4 sisa hasil bagi adalah 2 . Lalu indeks 2 dimasukkan kedalam variable Aku 
1.54
>>> type (Aku[a])#Menampilkan type data dari elemen tuple indeks a 
<type 'float'>
>>> Aku [a:4]#slicing dimulai indeks ke 2 sampai indeks ke 3
(1.54, 146)
>>> type (Aku[4])# menampilkan type data dari elemen tuple indeks 4
<type 'str'>
>>> Aku [0] = 'ok'# hasilnya ERROR karena elemenn sebuah tuple tidak dapat diubah

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Aku [0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type (Data)# menampilkan type data dari variable Data
<type 'list'>
>>> type (Data[4])#menampilka type data dari elemen list 4
<type 'str'>
>>> Data [4][5]#menampilkan list indeks 5 pada list 4
' '
>>> Data [4][a:6]#menampilkan list indeks 2 sampai 6 dari list 4
'tri '
>>> Data [0] = 'ok'; Data #merubah elemen list pada indeks 0 menjadi ok
['ok', 63, 1.54, 146, 'Putri Siwi Utami']
>>> Data [-a]# menampilkan huruf/angka terakhir pada indeks akhir ke 3 dari list
146
>>> range (a)#menampilkan semacam daftar atau koleksi dari indeks
[0, 1]
