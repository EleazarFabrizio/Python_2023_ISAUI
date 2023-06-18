
dicfggfgc = {

"131" : {"nombre" : "Coca-Cola 500ml" , "marca" : "Coca-Cola" , "precio" : 200 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"162" : {"nombre" : "Coca-Cola 2L" , "marca" : "Coca-Cola" , "precio" : 700 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"245" : {"nombre" : "Pringles" , "marca" : "Kellogg's" , "precio" : 500 , "stock" : 23 , "caracteristicas" : "Exceso de azucares y grasas"},
"371" : {"nombre" : "Pringles queso y cebolla" , "marca" : "Kellogg's" , "precio" : 670 , "stock" : 10 , "caracteristicas" : "Exceso de ricura"},
"490" : {"nombre" : "Doritos" , "marca" : "Pepsico" , "precio" : 570 , "stock" : 48 , "caracteristicas" : "Exceso en grasas"},
"490" : {"nombre" : "Lays" , "marca" : "Pepsico" , "precio" : 340 , "stock" : 47 , "caracteristicas" : "Exceso en grasas"},

}


def detalle(dicc):

    for z in range(0,len(dicc)):
        pass

    msj = "Codigo | Nombre | Marca | Precio | Stock | Caracteristicas\n\n"
    for i in dicc:
        msj = msj + " " + str(i) + "   | "
        for k in dicc[i]:
            msj = msj + str(dicc[i][k]) + " | "
        msj += "\n"

    print (msj)
