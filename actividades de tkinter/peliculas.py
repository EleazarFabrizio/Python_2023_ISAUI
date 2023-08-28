from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Peliculas")
root.resizable(0,0)

escribe = ttk.Label(root,text="Escribe el nombre de un pelicula",justify= CENTER , font=('Oswald',15)).grid(row=0,column=0,padx=(30,100),pady=(30,10))
pelicula = ttk.Label(root,text="Peliculas",justify= CENTER, font=('Oswald',15)).grid(row=0,column=1,padx=(0,30),pady=(30,10))

entry = ttk.Entry(root,font=('Oswald',15),justify=CENTER)
entry.grid(row=1,column=0,padx=(0,45))

root.mainloop()