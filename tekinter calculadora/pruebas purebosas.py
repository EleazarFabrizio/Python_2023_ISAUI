
from tkinter import  *

root = Tk()

display = Entry(root).grid(row= 0,column=0)

class Boton:
    def __init__(self,name,job,rou,col):
        self.name = name
        self.job = job
        self.rou = rou
        self.col = col



ejemplo = Boton("Jorge",56,0,1)

print(ejemplo.job)

root.mainloop()