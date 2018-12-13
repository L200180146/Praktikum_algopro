from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Luas Jajargenjang')

D = Label(my_app, text ='Luas Jajargenjang',font='Helvetica 20 bold')
D.grid(row=0, column=0)

D1 = Label(my_app, text ='Jajargenjang adalah bangun 2 dimensi ''\nJajargenjang memiliki 2 sisi,dan 4 titik sudut.',font='Helvetica 10')
D1.grid(columnspan=4,row=1, column=0)

L1 = Label (my_app, text = 'Tinggi : ')
L1.grid(row=2, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(columnspan=3 ,row=2, column=1)

L2 = Label (my_app, text = 'Alas : ')
L2.grid(row=3, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(columnspan=3 ,row=3, column=1)


def luas():
    t=float(str1.get())
    a=float(str2.get())
    ls=a*t
    LP.config(text=ls)

B = Button(my_app, text='Hitung Luas', command= luas)
B.grid(row=5,column=0)
L=Label(my_app, text='luas :',font='Helvetica 10 bold')
L.grid(row=5,column=2)
LP=Label(my_app, text='0')
LP.grid(row=5,column=3)

my_app.mainloop()
