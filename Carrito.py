
## PRE-ALPHA 0.0.1

import os
import fun_car

inventario = {

"131" : {"Codigo" : "131" , "Nombre" : "Coca-Cola 500ml" , "Marca" : "Coca-Cola" , "Precio" : 200.99 , "Stock" : 50 , "Caracteristicas" : "Exceso de azucares"},
"162" : {"Codigo" : "162" , "Nombre" : "Coca-Cola 2L" , "Marca" : "Coca-Cola" , "Precio" : 700.33 , "Stock" : 50 , "Caracteristicas" : "Exceso de azucares"},
"245" : {"Codigo" : "245" , "Nombre" : "Pringles" , "Marca" : "Kellogg's" , "Precio" : 500.45 , "Stock" : 23 , "Caracteristicas" : "Exceso de azucares y grasas"},
"371" : {"Codigo" : "371" , "Nombre" : "Pringles queso y cebolla" , "Marca" : "Kellogg's" , "Precio" : 670.00 , "Stock" : 10 , "Caracteristicas" : "Exceso de ricura"},
"490" : {"Codigo" : "490" , "Nombre" : "Doritos" , "Marca" : "Pepsico" , "Precio" : 570.50 , "Stock" : 48 , "Caracteristicas" : "Exceso en grasas"},
"780" : {"Codigo" : "780" , "Nombre" : "Lays" , "Marca" : "Pepsico" , "Precio" : 340.50 , "Stock" : 47 , "Caracteristicas" : "Exceso en grasas"},

}

compras_historicas = {}

carrito = {}

salir  = False

modo_de_busqueda = 1

total = 0

while salir == False:

    os.system("cls")

    carrito_print = ""

    print(f"""
    Bienvnido al carrito mas fachero del mundo mundial.
          
    Usted tiene el siguiente monto en compra: {total}

    1) Ver productos
    2) Ver carrito
    3) Ver compras historicas
    4) Salir:
    """)


    op = input(":   ")
    menu = True

    if op == "4":
        salir = True
        print ("bye bye!")
    
    elif op == "1":
        lista_return = fun_car.op1(inventario,modo_de_busqueda,menu,carrito)
        modo_de_busqueda = lista_return[0]
        inventario = lista_return[1]
        carrito = lista_return[2]

    elif op == "2":
        lista_return = fun_car.op2(inventario,modo_de_busqueda,carrito,menu,total,compras_historicas)
        modo_de_busqueda = lista_return[0]
        inventario = lista_return[1]
        carrito = lista_return[2]
        total=lista_return[4]
        compras_historicas = lista_return[5]

    elif op == "3":
        os.system("cls")
        if len(compras_historicas) == 0:
            space = input("Usted no ha realizado ninguna compra hasta la fecha.\nPrecione ENTER para continuar\n:   ")
        else:
            msj = ""
            for i in compras_historicas:
                print(compras_historicas[i])
            space = input("\nPrecione ENTER para continuar\n:   ")


    else:
        print("Opcion no valida. Precione cualquier tecla para continuar")
        op=input(": ")
        os.system("cls")
