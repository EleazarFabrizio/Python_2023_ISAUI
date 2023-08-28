from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Peliculas")
root.resizable(0,0)
s = ttk.Style()
s.configure('my.TButton', font=('Oswald', 15))

def ania():

    global peloquilas

    value = entry.get()
    peloquilas.insert(0,value)

escribe = ttk.Label(root,text="Escribe el nombre de un pelicula",justify= CENTER , font=('Oswald',15)).grid(row=0,column=0,padx=(30,30),pady=(30,10))
pelicula = ttk.Label(root,text="Peliculas",justify= CENTER, font=('Oswald',15)).grid(row=0,column=1,padx=(30,30),pady=(30,10))

entry = ttk.Entry(root,font=('Oswald',15),justify=CENTER)
entry.grid(row=1,column=0,padx=(30,30))

aniadir = ttk.Button(root,text="Añadir",style='my.TButton',command= lambda: ania()).grid(row=2,column=0,pady=(10,30))
peloquilas = Listbox(font=('Oswald',15),justify=CENTER,width=50)
peloquilas.grid(row=1,rowspan=3,column=1,padx=(0,30),pady=(0,30))

root.mainloop()