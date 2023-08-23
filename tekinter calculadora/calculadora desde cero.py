from tkinter import *

root = Tk()
root.title("Esta calculadora es una costra")
root.resizable(0, 0)
root.configure(bg="#555369")
#root.geometry("500x800")

display = Label(root,text="0",font=("Arial Black", 20), width=5, height=4,anchor="e", justify="right")

#DISPLAY DE NUMEROS MUY NUMEROSOS CON CARA DE OSO

display.grid(row=0,columnspan=6,sticky=W+E)

display_text = "0"

def escribir(v):
    list = ["7","8","9","4","5","6","(",")","1","2","3","*","/","0",".","+","-"]
    global display_text
    for i in list:
        if v == i:
            if (display_text == "0") or (display_text == "Error de sintaxis"):
                display_text = v
            else:
                display_text += v
    match v:
        case "DEL":
            display_text= display_text[:-1]
        case "AC":
            display_text = "0"
        case "=":
            try:
                display_text = str(eval(display_text))
            except:
                display_text = "Error de sintaxis"

    if len(display_text) == 0:
        display_text = "0"

    display.config(text= display_text)


list = ["7","8","9","DEL","AC","4","5","6","(",")","1","2","3","*","/","0",".","+","-","="]
botones=[]


conX = 0
conY = 0
for i in range (len(list)):
    
    botones.append(Button(root , text=list[i],font=("Arial Black", 20), width=5, height=3, command= lambda c = i: escribir(list[c])  ).grid(row=conX + 1,column=conY,padx=1,pady=1,sticky=W+E))
    conY += 1
    if conY > 4:
        conY = 0
        conX += 1

for i in botones:
    print(i)

root.mainloop()