
etiqueta = ["Codigo","Nombre","Marca","Cantidad","nose"]
canvas = [6,6,5,8,4]

productos = [[6789,"frijoles","toyota",9,"perro"],[0,"macarrones con queso","fordensio",9999999999,"uwu"]]

for i in range(0,len(productos)):
    for k in range(0,len(productos[i])):
        if len(str(productos[i][k])) > canvas[k]:
            canvas[k]=len(str(productos[i][k]))
            #print(productos[i][k])
            #print(len(str(productos[i][k])))

#print(canvas)

msj = ""

for i in range(0,len(etiqueta)):
    dividir = (canvas[i] - len(str(etiqueta[i]))) / 2
    msj+= " "*(round(dividir - 0.5)+1)
    msj+= str(etiqueta[i])
    msj+= " "*(round(dividir + 0.5)+1)
    msj+="|"
msj+="\n"

for i in range(0,len(productos)):
    for k in range(0,len(productos[i])):
        dividir = (canvas[k] - len(str(productos[i][k]))) / 2
        msj+= " "*(round(dividir - 0.5)+1)
        msj+= str(productos[i][k])
        msj+= " "*(round(dividir + 0.5)+1)
        msj+= "|"
    msj+="\n"

print(msj)