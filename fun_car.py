import os


def op1(inventario,modo_de_busqueda,menu):
    while menu == True:
        os.system("cls")
            
        detalle(inventario,modo_de_busqueda)

        if modo_de_busqueda == 1:
            op = input("\n\n1) Ver productos en breve\n2) Buscar producto\n3) Regresar\n:   ")
        else:
            op = input("\n\n1) Ver productos en detalle\n2) Buscar producto\n3) Regresar\n:   ")
        
        if op == "3":
            menu = False
        elif op == "1":
            if modo_de_busqueda == 1:
                modo_de_busqueda = 2
            else:
                modo_de_busqueda = 1
        elif op == "2":
            os.system("cls")
            buscar_producto(inventario,menu)
            
        else:
            print("Opcion no valida. Precione cualquier tecla para continuar")
            op=input(": ")
            os.system("cls")
    return modo_de_busqueda


##############################################################################################
##############################################################################################
##############################################################################################


def op2(inventario,modo_de_busqueda,carr,menu):
    while menu == True:
        os.system("cls")
        mostrar_carrito(carr)

        op = input("1) Ver productos\n2) Buscar producto\n3) Finalizar compra\n4) Regresar\n:   ")
        os.system("cls")
        if op == "4":
            menu = False
        elif op == "1":
            modo_de_busqueda=op1(inventario,modo_de_busqueda,menu)
        else:
            print("Opcion no valida. Precione cualquier tecla para continuar")
            op=input(": ")
            os.system("cls")
    return modo_de_busqueda
    

                
##############################################################################################
##############################################################################################
##############################################################################################


def detalle(dicc,tipe):
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

        if (tipe != 2) or ((i != 2) and (i != 5)):
            dividir = (espacios[i] - len(str(etiqueta[i]))) / 2
            msj+= " "*(round(dividir - 0.5)+1)
            msj+= str(etiqueta[i])
            msj+= " "*(round(dividir + 0.5)+1)
            msj+="|"

    msj+="\n|"
    for i in range(0,6):
        if (tipe != 2) or ((i != 2) and (i != 5)):
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
            if (tipe != 2) or ((con != 2) and (con != 5)):
                dividir = (espacios[con] - len(str(dicc[i][k]))) / 2
                msj+= " "*(round(dividir - 0.5)+1)
                msj+= str(dicc[i][k])
                msj+= " "*(round(dividir + 0.5)+1)
                msj+= "|"
            con += 1
        if decorar < 5:
            msj+="\n|"

    print(msj)


##############################################################################################
##############################################################################################
##############################################################################################


def mostrar_carrito(carr):
    if carr["total"] == 0:
        print("No tienes ningun producto en tu carrito\n\n")

















##############################################################################################
##############################################################################################
##############################################################################################


def buscar_producto(inventario,menu):
    while menu == True:

        os.system("cls")

        detalle(inventario,1)

        cod=input("\nPor favor ingrese un producto por codigo o nombre\n0) Regresar\n: ")

        if cod == "0":
            menu = False
            os.system("cls")
        
        else:
            encontrado = False
            for i in inventario:
                if (i == cod) or (inventario[i]["nombre"] == cod):
                    encontrado = True

            if encontrado == True:
                
                second_menu = True
                while second_menu == True:
                    op = input("Producto encontrado\n\n1) Agregar producto al carrito\n2) Regresar\n:   ")

                    if op == "2":
                        second_menu = False

                    elif op == "1":
                        op = input("¿Serguro desea ingresar este producto a su carrito de compra?\n\n1) SI      2) NO\n:")
                        if (op == "1") or (op.lower() == "si"):
                            second_menu = False
                            print("Producto ingresado correctamente")
                        elif (op == "2") or (op.lower() == "no"):
                            second_menu = False
                        else:
                            print("Opcion no valida")
                            
                    else:
                        print ("Valor ingresado no es valido\n: ")
            else:
                op = input("Producto no encontrado. Asegurese de ingresar un codigo valido\nPrecione cualquier tecla para continuar:  ")













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