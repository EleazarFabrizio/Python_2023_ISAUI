from tkinter import *

root = Tk()

root.title("Contador de su servidor Eleazar carita feliz")
root.resizable(0, 0)

numero = StringVar()
numero.set(0)

def editar(i):
    global numero
    g = int(numero.get())
    match i:
        case 0:
            numero.set(g + 1)
        case 1:
            numero.set(g - 1)
        case 2:
            numero.set(0)

label_n = Label(root,text="Contador",font=('Oswald',15)).grid(row=0, column= 0 ,padx=(30,10),pady=100)

num_entry = Entry(root, state="readonly",font=('Oswald',15),width=15,textvariable=numero , justify=CENTER)
num_entry.grid(row=0, column= 1,padx=(0,10),pady=0)


Count_Up = Button(root,text="Count Up",font=('Oswald',15),command= lambda : editar(0)).grid(row=0, column= 3 ,padx=(0,10))
Count_Down = Button(root,text="Count Down",font=('Oswald',15),command= lambda : editar(1)).grid(row=0, column= 4 ,padx=(0,10))
Reset = Button(root,text="Reset",font=('Oswald',15),command= lambda : editar(2)).grid(row=0, column= 5 ,padx=(0,30))
    
root.mainloop()