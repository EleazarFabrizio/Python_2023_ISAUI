import os


def op1(inventario,modo_de_busqueda,menu,carr):
    
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
            return_buscar = buscar_producto(inventario,menu,carr)
            ##menu = return_buscar[2]
            inventario = return_buscar[0]
            carr = return_buscar[1]

            
        else:
            space = input("Opcion no valida. Precione ENTER para continuar\n:   ")
            os.system("cls")

    lista_return = [modo_de_busqueda,inventario,carr,menu]
    return lista_return


##############################################################################################
##############################################################################################
##############################################################################################


def op2(inventario,modo_de_busqueda,carr,menu,total,historial):
    
    while menu == True:
        os.system("cls")
        
        return_carrito = mostrar_carrito(carr,total)
        carr = return_carrito[1]
        total = return_carrito[0]

        op = input("1) Ver productos\n2) Editar Productos\n3) Finalizar compra\n4) Regresar\n:   ")
        os.system("cls")
        if op == "4":
            menu = False
        elif op == "1":
            return_op1 = op1(inventario,modo_de_busqueda,menu,carr)
            modo_de_busqueda = return_op1[0]
            inventario = return_op1[1]
            carr = return_op1[2]

        elif op == "2":
            os.system("cls")
            mostrar_carrito(carr,total)
            buscando = True
            while buscando == True:
                cod = input("Ingrese el codigo del producto al que desea editar\n:  ")
                if cod in carr == False:
                    space = input("No hay ningun producto en su carrito de compra con ese codigo. Precione ENTER para continuar\n:  ")
                else:
                    buscando = False

                    ingresando = True
                    while ingresando == True:
                        num = input("Ingrese la cantidad de items que desea eliminar de este producto en su carrito.\n:     ")
                        if num.isnumeric() == False:
                            print("\nDebe ingresar un numero entero. Precione ENTER para continuar\n:   ")
                        else:
                            num = int(num)

                            if num >= carr[cod]["Cantidad"]:
                                print("Usted estaria eliminanddo el producto por completo de su carrito.")
                                num = carr[cod]["Cantidad"]

                            op = si_o_no("\nSeguro desea realizar estos cambios?\n1) SI         2)NO\n\n:   ")
                            if op == 2:
                                space = input("No se han realizado cambios. Precione ENTER para continuar\n:  ")
                            else:
                                regresar = num 
                                inventario[cod]["Stock"] = inventario[cod]["Stock"] + regresar
                                carr[cod]["Cantidad"] = carr[cod]["Cantidad"] - num
                                carr[cod]["Subtotal"] = carr[cod]["Cantidad"] * carr[cod]["Precio x Unidad"]
                                if carr[cod]["Cantidad"] <= 0:
                                    carr.pop(cod)
                                space = input("Los cambios se han realizado exitosamente. Precione ENTER para continuar\n:  ")
                            ingresando = False



            #menu = False
        
        elif op == "3":
            op = si_o_no("\nEsta seguro que desea finalizar esta compra?\n1) SI          2) NO\n:    ")

            if op == 1:
                msj = f"""\nCompra numero : {str(len(historial)+1)}\nTotal de compra : ${str(total)}"""
                msj += detalle_compra(carr)
                historial[len(historial)+1] = msj
                carr.clear()
                space = input("Se ha finalizado la compra exitosamente. Precione ENTER para continuar\n:  ")

        else:
            space = input("Opcion no valida. Precione ENTER para continuar\n:   ")
            os.system("cls")

    lista_return = [modo_de_busqueda,inventario,carr,menu,total,historial]
    return lista_return
    

                
##############################################################################################
##############################################################################################
##############################################################################################


def detalle(dicc,tipe):

    etiqueta = ["Codigo","Nombre","Marca","Precio","Stock","caracteristicas"]
    espacios = [6,6,5,6,5,15]
    

    #tipo == 2 and con != 2 or con!= 5

    for i in dicc:
        con = 0
        dicc[i]["Precio"] = "$" + str(dicc[i]["Precio"])
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
        con = 0

        for k in dicc[i]:
            if (tipe != 2) or ((con != 2) and (con != 5)):
                dividir = (espacios[con] - len(str(dicc[i][k]))) / 2
                msj+= " "*(round(dividir - 0.5)+1)
                msj+= str(dicc[i][k])
                msj+= " "*(round(dividir + 0.5)+1)
                msj+= "|"
            con += 1
        if decorar < len(dicc):
            msj+="\n|"

    for i in dicc:
        dicc[i]["Precio"] = float(dicc[i]["Precio"].replace("$",""))

    print(msj)


##############################################################################################
##############################################################################################
##############################################################################################


def detalle_compra(dicc):

    
    etiqueta = ["Codigo","Nombre","Precio x Unidad","Cantidad","Subtotal"]
    espacios = [6,6,15,8,8]


    for i in dicc:
        dicc[i]["Precio x Unidad"] = "$" + str(dicc[i]["Precio x Unidad"])
        con = 0
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
    for i in range(0,5):
        msj+= " "*(espacios[i]+2)
        msj+="|"
    msj+="\n|"

    decorar = 0
    for i in dicc:
        decorar += 1
        con = 0

        for k in dicc[i]:
            
            dividir = (espacios[con] - len(str(dicc[i][k]))) / 2
            msj+= " "*(round(dividir - 0.5)+1)
            msj+= str(dicc[i][k])
            msj+= " "*(round(dividir + 0.5)+1)
            msj+= "|"
            con += 1
        if decorar < len(dicc):
            msj+="\n|"

    for i in dicc:
        dicc[i]["Precio x Unidad"] = float(dicc[i]["Precio x Unidad"].replace("$",""))

    return msj


##############################################################################################
##############################################################################################
##############################################################################################


def mostrar_carrito(carr,total):

    
    total = 0.0

    for i in carr:
        total += float(carr[i]["Subtotal"])

    os.system("cls")
    
    if len(carr) == 0:
        print("No tienes ningun producto en tu carrito\n\n")
    else:
        msj = (f"""Su total de compra es igual a: {total}\n""")
        msj += detalle_compra(carr)
        msj += "\n"
        print(msj)


    lista_return = [total,carr]
    return lista_return


##############################################################################################
##############################################################################################
##############################################################################################


def si_o_no(txt):
    flag = True
    while flag == True:
        op = input(txt)

        op = op.lower()

        if (op == "1") or (op == "si"):
            answer = 1
            flag = False
        elif (op == "2") or (op == "no"):
            answer = 2
            flag = False
        else:
            print("opcion ingresada no es valida")
    
    return answer


##############################################################################################
##############################################################################################
##############################################################################################


def buscar_producto(inventario,menu,carr):
    
    while menu == True:

        os.system("cls")

        detalle(inventario,1)

        cod=input("\nPor favor ingrese un producto por codigo o nombre\n00) Regresar\n\n:    ")

        if cod == "00":
            menu = False
            os.system("cls")
        
        else:
            encontrado = False
            for i in inventario:
                if (cod == i) or (cod.lower() == str(inventario[i]["Nombre"]).lower()):
                    encontrado = True
                    key = i

            if encontrado == False:
                op = input("\nProducto no encontrado. Asegurese de ingresar un codigo valido\nPrecione cualquier tecla para continuar:  ")
            else:
                op = input("\nProducto encontrado\n\n1) Agregar producto al carrito\n2) Regresar\n:   ")

                if op == "2":
                    menu = False
                if op == "1":
                    op = si_o_no("Esta seguro de agregar este producto a su carrito?\n\n1) SI               2) NO\n\n:  ")
                    
                    if op == 1:
                        agregar = True
                        while agregar == True:
                            num = input("Ingrese la cantidad que desea comprar\n:   ")

                            if num.isnumeric() == False:
                                print("Cantidad ingresada debe ser un numero entero")

                            else:
                                num = int(num)
                                if num <= 0:
                                    space = ("No se ha agregado ningun producto a su carrito\n\n:   ")
                                    agregar = False

                                elif (num > inventario[key]["Stock"]):
                                    print("La cantidad que desea agregar supera el stock siponible")
                                else:
                                    if key in carr:
                                        carr[key]["Cantidad"] += num
                                        carr[key]["Subtotal"] = (carr[key]["Precio x Unidad"] * carr[key]["Cantidad"])
                                    else:
                                        carr[key] = {  "Codigo" : key , "Nombre" : inventario[key]["Nombre"] , "Precio x Unidad" : inventario[key]["Precio"], "Cantidad" : num , "Subtotal" : ((inventario[key]["Precio"]) * num)}
                                    inventario[key]["Stock"] -= num
                            
                                    space = input("Producto agregado al carrito exitosamente. Precione ENTER para continuar")

                                    agregar = False
                    menu = False

    lista_return = [inventario,carr,menu]
    return lista_return


##############################################################################################
##############################################################################################
##############################################################################################















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