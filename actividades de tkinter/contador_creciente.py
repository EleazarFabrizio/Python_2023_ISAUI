
from tkinter import *
    
root = Tk()

root.title("ContCreciente de Eleazar")
root.resizable(0, 0)
root.geometry("500x200")

con = 0
conn = StringVar()
conn.set(0)

contador = Label(root,text= "contador:",font=("Oswald", 15),width=10, height=5)
contador.pack()

entrada = Entry(root,state="readonly",textvariable=conn)
entrada.pack()

def sumar():
    global con
    try:
        con = int(entrada.get())
        con += 1
        conn.set(con)
    except:
        conn.set("Ingrese un numero")
    


boton = Button(root,text="+",command= lambda: sumar())
boton.pack()

root.mainloop()