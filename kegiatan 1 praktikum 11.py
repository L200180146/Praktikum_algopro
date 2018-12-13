# window dengan tombol, beberapa kotak edit dan label
from Tkinter import Tk, Label, Entry, Button
from tkMessageBox import showinfo


my_app = Tk(className='Aplikasi dengan beberapa widget')
L0 = Label(my_app, text='Data diri', font=('Arial', 24))
L0.grid(row=0, column=0)
L1 = Label(my_app, text="Nama mahasiswa")
L1.grid(row=1, column=0)
E1 = Entry(my_app)
E1.grid(row=1, column=1                    )
L2 = Label(my_app, text="NIM")
L2.grid(row=2, column=0)
E2 = Entry(my_app)
E2.grid(row=2, column=1)
L3 = Label(my_app, text="Buku favorite")
L3.grid(row=3, column=0)
E3 = Entry(my_app)
E3.grid(row=3, column=1)
L4 = Label(my_app, text="Idola di kalangan sahabat")
L4.grid(row=4, column=0)
E4 = Entry(my_app)
E4.grid(row=4, column=1)
L5 = Label(my_app, text="Motto")
L5.grid(row=5, column=0)
E5 = Entry(my_app)
E5.grid(row=5, column=1)

def tampil_pesan():
    showinfo("Pesan", "Hello World")

B = Button(my_app, text="Tutup", command=my_app.quit())
B.grid(row=6, column=1)
my_app.mainloop()
