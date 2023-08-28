
from tkinter import *
from tkinter import ttk
import random

root = Tk()

root.title("Generador de numero Aleatorios de Eleazar")
root.resizable(0,0)
s = ttk.Style()
s.configure('my.TButton', font=('Oswald', 15))

spin_1 = StringVar()
spin_1.set(0)
spin_2 = StringVar()
spin_2.set(0)
resultado_random = StringVar()

def gen_ran():
    global resultado
    
    prim = int(primer_spin.get())
    seg = int(segundo_spin.get())
    if seg > prim:
        value = random.randint(prim,seg)
    else:
        value = random.randint(seg,prim)

    resultado_random.set(value)


ttk.Label(root,text="Numero 1",style='my.TButton',justify=CENTER).grid(row=0,column=0,padx=(30,0),pady=(30,10))
primer_spin = Spinbox(root,textvariable=spin_1,from_=-100,to=100,increment=1,font=('Oswald',15),justify=CENTER)
primer_spin.grid(row=0,column=1,padx=(10,30),pady=(30,10))

ttk.Label(root,text="Numero 2",style='my.TButton',justify=CENTER).grid(row=1,column=0,padx=(30,0),pady=(0,30))
segundo_spin = Spinbox(root,textvariable=spin_2,from_=-100,to=100,increment=1,font=('Oswald',15),justify=CENTER)
segundo_spin.grid(row=1,column=1,padx=(10,30),pady=(0,30))

ttk.Label(root,text="Numero Generado",style='my.TButton',justify=CENTER).grid(row=3,column=0,padx=(30,0),pady=(0,10))
resultado = ttk.Entry(root,font=('Oswald',15),state="readonly",textvariable=resultado_random)
resultado.grid(row=3,column=1,padx=(10,30),pady=(0,10),sticky=W+E)

generar = ttk.Button(root,style='my.TButton',text="Generar",command= lambda: gen_ran()).grid(row=4,column=1,padx=(0,30),pady=(0,30))

root.mainloop()