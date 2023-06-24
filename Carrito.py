
## PRE-ALPHA 0.0.1

import os
import fun_car

inventario = {

"131" : {"Nombre" : "Coca-Cola 500ml" , "Marca" : "Coca-Cola" , "Precio" : 200 , "Stock" : 50 , "Caracteristicas" : "Exceso de azucares"},
"162" : {"Nombre" : "Coca-Cola 2L" , "Marca" : "Coca-Cola" , "Precio" : 700 , "Stock" : 50 , "Caracteristicas" : "Exceso de azucares"},
"245" : {"Nombre" : "Pringles" , "Marca" : "Kellogg's" , "Precio" : 500 , "Stock" : 23 , "Caracteristicas" : "Exceso de azucares y grasas"},
"371" : {"Nombre" : "Pringles queso y cebolla" , "Marca" : "Kellogg's" , "Precio" : 670 , "Stock" : 10 , "Caracteristicas" : "Exceso de ricura"},
"490" : {"Nombre" : "Doritos" , "Marca" : "Pepsico" , "Precio" : 570 , "Stock" : 48 , "Caracteristicas" : "Exceso en grasas"},
"780" : {"Nombre" : "Lays" , "Marca" : "Pepsico" , "Precio" : 340 , "Stock" : 47 , "Caracteristicas" : "Exceso en grasas"},

}


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

    {carrito_print}

    1) Ver productos
    2) Ver carrito
    3) Salir:
    """)


    op = input(":   ")
    menu = True

    if op == "3":
        salir = True
        print ("bye bye!")
    
    elif op == "1":
        lista_return = fun_car.op1(inventario,modo_de_busqueda,menu,carrito)
        modo_de_busqueda = lista_return[0]
        inventario = lista_return[1]
        carrito = lista_return[2]

    elif op == "2":
        lista_return = fun_car.op2(inventario,modo_de_busqueda,carrito,menu,total)
        modo_de_busqueda = lista_return[0]
        inventario = lista_return[1]
        carrito = lista_return[2]
        total=lista_return[4]



    else:
        print("Opcion no valida. Precione cualquier tecla para continuar")
        op=input(": ")
        os.system("cls")
