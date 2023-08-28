from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Calculadora de bajo presupuesto de Eleazar")
root.resizable(0,0)
s = ttk.Style()
s.configure('my.TButton', font=('Oswald', 20))

resultado = StringVar()
resultado.set(0)

def edit(i):
    try:
        pri = int(primer_entry.get())
        seg = int(segundo_entry.get())
        match i:
            case 0:
                resultado.set(pri + seg)
            case 1:
                resultado.set(pri - seg)
            case 2:
                resultado.set(pri * seg)
            case 3:
                resultado.set(pri / seg)
            case 4:
                resultado.set((pri * seg) / 100)
            case 5:
                resultado.set(0)
                primer_entry.delete(0,END)
                segundo_entry.delete(0,END)
    except:
        resultado.set("Error de syntaxis")


primer_label = ttk.Label(root,text="Primer Numero",font=('Oswald',15)).grid(row=0, column= 0 ,padx=(30,10),pady=(30,0))

primer_entry = ttk.Entry(root,font=('Oswald',15),width=15 , justify=CENTER)
primer_entry.grid(row=0,column=1,padx=(0,30),pady=(30,0))

segundo_label = ttk.Label(root,text="Segundo Numero",font=('Oswald',15)).grid(row=1, column= 0 ,padx=(30,10),pady=0)

segundo_entry = ttk.Entry(root,font=('Oswald',15),width=15 , justify=CENTER)
segundo_entry.grid(row=1,column=1,padx=(0,30),pady=0)

resultado_label = ttk.Label(root,text="Resultado",font=('Oswald',15)).grid(row=2, column= 0 ,padx=(30,10),pady=(0,30))
resultado_entry = ttk.Entry(root,font=('Oswald',15),width=15, state="readonly",textvariable=resultado, justify=CENTER).grid(row=2,column=1,padx=(0,30),pady=(0,30))

sumar = ttk.Button(root,text="+",style='my.TButton',command= lambda: edit(0)).grid(row= 3,column= 0,padx=10,pady=10,sticky=W+E)
restar = ttk.Button(root,text="-",style='my.TButton',command= lambda: edit(1)).grid(row= 3,column= 1,padx=10,pady=10,sticky=W+E)
multiplicar = ttk.Button(root,text="*",style='my.TButton',command= lambda: edit(2)).grid(row= 4,column= 0,padx=10,pady=10,sticky=W+E)
dividir = ttk.Button(root,text="/",style='my.TButton',command= lambda: edit(3)).grid(row= 4,column= 1,padx=10,pady=10,sticky=W+E)
porcentaje = ttk.Button(root,text="%",style='my.TButton',command= lambda: edit(4)).grid(row= 5,column= 0,padx=10,pady=10,sticky=W+E)
clear = ttk.Button(root,text="CLEAR",style='my.TButton',command= lambda: edit(5)).grid(row= 5,column= 1,padx=10,pady=10,sticky=W+E)

root.mainloop()