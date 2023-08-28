
from tkinter import *

root = Tk()

root.title("Factorial de adivina quien")
root.resizable(0, 0)
#root.geometry("800x300")

n = StringVar()
n.set(1)
f = StringVar()
f.set(1)

def sumar():
    global n
    global f

    m = int(n.get())
    g = int(f.get())
    n.set(m + 1)
    f.set(g*(m+1))



label_n = Label(root,text="n",font=('Oswald',15)).grid(row=0, column= 0 ,padx=(30,0))

n_entry = Entry(root, state="readonly",font=('Oswald',15),width=5,textvariable=n , justify=CENTER)
n_entry.grid(row=0, column= 1,padx=0,pady=100)

label_factor = Label(root,text="Factorial (n)",font=('Oswald',15)).grid(row=0, column= 3 ,padx=(30,0))

fac_entry = Entry(root, state="readonly",font=('Oswald',15),width=15,textvariable=f , justify=CENTER)
fac_entry.grid(row=0, column= 4,padx=(0,30),pady=100)

boton = Button(root,text="Siguiente",font=('Oswald',15),command= lambda: sumar()).grid(row=0, column= 5 ,padx=(0,30))

root.mainloop()