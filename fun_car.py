


def breve(dicc):

    for z in range(0,len(dicc)):
        pass

    msj = "Codigo | Nombre | Marca | Precio | Stock | Caracteristicas\n\n"
    for i in dicc:
        msj = msj + " " + str(i) + "   | "
        for k in dicc[i]:
            msj = msj + str(dicc[i][k]) + " | "
        msj += "\n"

    print (msj)

##############################################################################################
##############################################################################################
##############################################################################################

def detalle(dicc):
    etiqueta = ["Codigo","Nombre","Marca","Precio","Stock","caracteristicas"]
    espacios = [6,6,5,6,5,15]

    #tipo == 2 and con != 2 or con!= 5

    for i in dicc:
        con = 1

        if len(str(i)) > espacios[0]:
            espacios[0] = len(str(i))

        for k in dicc[i]:
            if len(str(dicc[i][k])) > espacios[con]:
                espacios[con]=len(str(dicc[i][k]))
            con+=1

    msj = "\n|"

    for i in range(0,len(etiqueta)):
        dividir = (espacios[i] - len(str(etiqueta[i]))) / 2
        msj+= " "*(round(dividir - 0.5)+1)
        msj+= str(etiqueta[i])
        msj+= " "*(round(dividir + 0.5)+1)
        msj+="|"
    msj+="\n|"
    for i in range(0,6):
        msj+= " "*(espacios[i]+2)
        msj+="|"
    msj+="\n|"

    decorar = 0
    for i in dicc:
        decorar += 1
        con = 1

        dividir = (espacios[0] - len(str(i))) / 2
        msj+= " "*(round(dividir - 0.5)+1)
        msj+= str(i)
        msj+= " "*(round(dividir + 0.5)+1)
        msj+= "|"

        for k in dicc[i]:
            dividir = (espacios[con] - len(str(dicc[i][k]))) / 2
            msj+= " "*(round(dividir - 0.5)+1)
            msj+= str(dicc[i][k])
            msj+= " "*(round(dividir + 0.5)+1)
            msj+= "|"
            con += 1
        if decorar < 5:
            msj+="\n|"

    print(msj)


"""etiqueta = ["Codigo","Nombre","Marca","Cantidad","nose"]
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

print(msj)"""