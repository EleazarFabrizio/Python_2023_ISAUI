
from tkinter import  *

root = Tk()

pollo = Listbox(root)
pollo.grid(row=0,column=0)
pollo.insert(0,"HOLA")

root.mainloop()