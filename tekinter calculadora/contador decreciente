
from tkinter import *
    
root = Tk()

root.title("ContDecreciente de Eleazar")
root.resizable(0, 0)
root.geometry("500x200")

con = 88
conn = StringVar()
conn.set(con)

contador = Label(root,text= "contador:",font=("Oswald", 15),width=10, height=5)
contador.pack()

entrada = Entry(root,state="readonly",textvariable=conn)
entrada.pack()

def sumar():
    global con
    con -= 1
    conn.set(con)


boton = Button(root,text="-",command= lambda: sumar())
boton.pack()

root.mainloop()