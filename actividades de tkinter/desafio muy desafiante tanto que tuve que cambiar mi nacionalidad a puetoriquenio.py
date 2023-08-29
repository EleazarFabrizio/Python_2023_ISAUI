from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.resizable(0,0)
root.title("Desafió tan difícil que la tierra es un paramo inhóspito de vida después del mal que este desafió libro sobre nuestras pobres almas.")

num1 = IntVar()
num2 = IntVar()
num3 = StringVar() ; num3.set("")
op = IntVar() ; op.set(None)
dif = IntVar() ; dif.set(1)
puntos = [0,0,0]

s = ttk.Style() ; s.configure('my.TButton', font=('Oswald', 15)) ; s.configure('BW.TRadiobutton', font=('Oswald', 15))

lista_operaciones = ["+","-","*","/"]

def arreglar(num):
    x = num
    if "." in str(x):
        separado = str(x)
        separado = separado.replace("." , " ")
        separado = separado.split()
        if int(separado[1]) == 0:
            x = int(separado[0])
        
        else:
            periodo = ""
            anterior = []
            for i in separado[1]:
                if i in anterior:
                    return( float(separado[0] + "." + periodo))
                else:
                    periodo += i
                    anterior.append(i)
            x = float(separado[0] + "." + periodo)

    return x


def nuevo():
    op.set(random.randint(0,3))
    dificultad = dif.get()
    tope = int("10" + ("0"*dificultad))
    num1.set(random.randint(1,tope))
    num2.set(random.randint(1,tope))
    num3.set("")
    signo.config(text=lista_operaciones[op.get()])
    
def resolver():
    calculo = arreglar(eval(str(num1.get()) +  lista_operaciones[op.get()] + str(num2.get())))
    #truncar = calculo // 0.1 / 100
    try:
        if "." in str(calculo):
            respuesta_correcta = (    (       str(calculo)     ).replace("."," ")      ).split()
            print("ES FLOTANTE")
            print(type(respuesta_correcta))

            if "." in num3.get():
                mi_respuesta = (    (       num3.get()     ).replace("."," ")      ).split()
                print(len(mi_respuesta))
                print(mi_respuesta[0] == respuesta_correcta[0])
                if (mi_respuesta[0] == respuesta_correcta[0]) and (len(mi_respuesta) == 2):
                    #print("SIIIIIIIII")
                    #print(respuesta_correcta)
                    #print(mi_respuesta)
                    condicion2 = True
                    if len(mi_respuesta[1]) < len(respuesta_correcta[1]):
                        menor = len(mi_respuesta[1])
                    else:
                        menor = len(respuesta_correcta[1])
                    for i in range(0,menor):
                        if mi_respuesta[1][i] != respuesta_correcta[1][i]:
                            condicion2 = False
                    #print(condicion2)

                    if condicion2 == True:
                        puntos[1] += 1

                else:
                    puntos[2] += 1
            else:
                puntos[2] += 1

        elif float(num3.get()) == calculo:
            puntos[1] += 1
        else:
            puntos[2] += 1
            #print (num3.get())
            #print(calculo)
        puntos[0] += 1
        puntuacion.config(text=f"Juegos: {puntos[0]}\nBuenos: {puntos[1]}\nMalos: {puntos[2]}")

        nuevo()

    except:
        pass

primer = ttk.Entry(root,font=('Oswald',15),textvariable=num1,state='readonly',justify=CENTER,width=20) ; primer.grid(row=0,column=0,padx=(30,10),pady=(30,10))

signo = ttk.Label(root,text="?",font=('Oswald',15))
signo.grid(row=0,column=1,padx=(0,10),pady=(30,10))

segundo = ttk.Entry(root,font=('Oswald',15),textvariable=num2, state='readonly',justify=CENTER,width=20) ; segundo.grid(row=0,column=2,padx=(10,30),pady=(30,10))

ttk.Button(root,text="Nuevo numero",style=('my.TButton'),width=20,command= lambda: nuevo()).grid(row=1,column=3,padx=(50,30),pady=(0,50))



ttk.Radiobutton(root,text="Sumar",style='BW.TRadiobutton',value=[0],variable=op,state=DISABLED).grid(row= 2,column=0,sticky=W,padx=(95,0))
ttk.Radiobutton(root,text="Restar",style='BW.TRadiobutton',value=[1],variable=op,state=DISABLED).grid(row= 3,column=0,sticky=W,padx=(95,0))
ttk.Radiobutton(root,text="Multiplicar",style='BW.TRadiobutton',value=[2],variable=op,state=DISABLED).grid(row= 4,column=0,sticky=W,padx=(95,0))
ttk.Radiobutton(root,text="Dividir",style='BW.TRadiobutton',value=[3],variable=op,state=DISABLED).grid(row= 5,column=0,sticky=W,padx=(95,0))

resultado_entry = ttk.Entry(root,font=('Oswald',15),textvariable=num3,justify=CENTER,width=20)
resultado_entry.grid(row=2,column=3,rowspan=2,columnspan=2,padx=(20,0))

ttk.Button(root,text="Resultado",style=('my.TButton'),command= lambda: resolver(),width=20).grid(row=4,column=3,padx=(20,0))

puntuacion = ttk.Label(root,text="Juegos: 0\nBuenos: 0\nMalos: 0",font=('Oswald',15)) ; puntuacion.grid(row=6,column=3,rowspan=2,padx=(20,0),pady=(30,30))

ttk.Radiobutton(root,text="Facil",style='BW.TRadiobutton',value=[0],variable=dif).grid(row= 7,column=0,sticky=W,padx=(50,0))
ttk.Radiobutton(root,text="Normal",style='BW.TRadiobutton',value=[1],variable=dif).grid(row= 7,column=0,sticky=W,padx=(125,0))
ttk.Radiobutton(root,text="Dificil",style='BW.TRadiobutton',value=[2],variable=dif).grid(row= 7,column=0,sticky=W,padx=(225,0))


root.mainloop()