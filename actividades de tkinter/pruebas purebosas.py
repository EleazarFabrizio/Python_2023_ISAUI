
from tkinter import  *

root = Tk()

def hola():
    value = entry.get()
    print(value)

entry = Entry(root)
entry.grid(row=0,column=0,padx=20,pady=20)

boton = Button(text="HOLA",command=hola).grid(row=1,column=0,padx=20,pady=20)

root.mainloop()