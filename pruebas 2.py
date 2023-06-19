from os import system

inven = {

"131" : {"nombre" : "Coca-Cola 500ml" , "marca" : "Coca-Cola" , "precio" : 200 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"162" : {"nombre" : "Coca-Cola 2L" , "marca" : "Coca-Cola" , "precio" : 700 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"245" : {"nombre" : "Pringles" , "marca" : "Kellogg's" , "precio" : 500 , "stock" : 23 , "caracteristicas" : "Exceso de azucares y grasas"},
"371" : {"nombre" : "Pringles queso y cebolla" , "marca" : "Kellogg's" , "precio" : 670 , "stock" : 10 , "caracteristicas" : "Exceso de ricura"},
"490" : {"nombre" : "Doritos" , "marca" : "Pepsico" , "precio" : 570 , "stock" : 48 , "caracteristicas" : "Exceso en grasas"},
"490" : {"nombre" : "Lays" , "marca" : "Pepsico" , "precio" : 340 , "stock" : 47 , "caracteristicas" : "Exceso en grasas"},

}
33333
etiqueta = ["Codigo","Nombre","Marca","Precio","Stock","caracteristicas"]
espacios = [6,6,5,6,5,15]

def detalle(dicc):
    etiqueta = ["Codigo","Nombre","Marca","Precio","Stock","caracteristicas"]
    espacios = [6,6,5,6,5,15]
    ######## = [0,1,2,3,4,5]

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

        if (i != 2) and (i != 5):
            dividir = (espacios[i] - len(str(etiqueta[i]))) / 2
            msj+= " "*(round(dividir - 0.5)+1)
            msj+= str(etiqueta[i])
            msj+= " "*(round(dividir + 0.5)+1)
            msj+="|"

    msj+="\n|"
    for i in range(0,6):

        if (i != 2) and (i != 5):
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
                
            if (con != 2) and (con != 5):
                dividir = (espacios[con] - len(str(dicc[i][k]))) / 2
                msj+= " "*(round(dividir - 0.5)+1)
                msj+= str(dicc[i][k])
                msj+= " "*(round(dividir + 0.5)+1)
                msj+= "|"
            con += 1
        if decorar < 5:
            msj+="\n|"

    print(msj)














system("cls")

detalle(inven)