from tkinter import *
from tkinter import ttk
import random

root = Tk()

root.title("Calculadora dos de Eleazar")
root.resizable(0,0)
s = ttk.Style()
s.configure('my.TButton', font=('Oswald', 15))
s.configure('BW.TRadiobutton', font=('Oswald', 15))

resultado = StringVar()
resultado.set(0)

op = IntVar()
oper =  ["+","-","*","/"]

def edit():
    global res_entry
    i = op.get()
    try:
        pri = val1_entry.get()
        seg = val2_entry.get()
        resol = eval(pri + oper[i-1] + seg)
        resultado.set(resol)

    except:
        resultado.set("Error de syntaxis")


val1_label = ttk.Label(root,text="Valor 1",style='my.TButton').grid(row=0,column=0,padx=(30,10),pady=(30,10))
val1_entry = ttk.Entry(root,style='my.TButton',font=('Oswald',15),justify=CENTER)
val1_entry.grid(row=0,column=1,padx=(0,30),pady=(30,10))

val2_label = ttk.Label(root,text="Valor 2",style='my.TButton').grid(row=1,column=0,padx=(30,10),pady=(0,10))
val2_entry = ttk.Entry(root,style='my.TButton',font=('Oswald',15),justify=CENTER)
val2_entry.grid(row=1,column=1,padx=(0,30),pady=(0,10))

res_label = ttk.Label(root,text="Resultado",style='my.TButton').grid(row=2,column=0,padx=(30,10),pady=(0,30))
res_entry = ttk.Entry(root,style='my.TButton',font=('Oswald',15),justify=CENTER,state='readonly',textvariable=resultado)
res_entry.grid(row=2,column=1,padx=(0,30),pady=(0,30))

op_label = ttk.Label(root,text="Operaciones",style='my.TButton').grid(row=0,column=2,padx=(0,30),pady=(30,10))

radio_name = ["Sumar","Restar","Multiplicar","Dividir"]


for i in range(len(radio_name)):
    rt = ttk.Radiobutton(root,text=radio_name[i],style='BW.TRadiobutton',value=[i+1],variable=op).grid(row= 1+i, column= 2,pady=(10,30))

cal_butt = ttk.Button(root,text="Calcular",style='my.TButton',command= lambda: edit()).grid(row=4,column=0,pady=(0,30))

root.mainloop()