
## PRE-ALPHA 0.0.1

import os
import fun_car

inventario = {

"131" : {"nombre" : "Coca-Cola 500ml" , "marca" : "Coca-Cola" , "precio" : 200 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"162" : {"nombre" : "Coca-Cola 2L" , "marca" : "Coca-Cola" , "precio" : 700 , "stock" : 50 , "caracteristicas" : "Exceso de azucares"},
"245" : {"nombre" : "Pringles" , "marca" : "Kellogg's" , "precio" : 500 , "stock" : 23 , "caracteristicas" : "Exceso de azucares y grasas"},
"371" : {"nombre" : "Pringles queso y cebolla" , "marca" : "Kellogg's" , "precio" : 670 , "stock" : 10 , "caracteristicas" : "Exceso de ricura"},
"490" : {"nombre" : "Doritos" , "marca" : "Pepsico" , "precio" : 570 , "stock" : 48 , "caracteristicas" : "Exceso en grasas"},
"490" : {"nombre" : "Lays" , "marca" : "Pepsico" , "precio" : 340 , "stock" : 47 , "caracteristicas" : "Exceso en grasas"},

}

salir  = False

modo_de_busqueda = 1

while salir == False:    
    os.system("cls")

    carrito = {
    "total" : 0
    }

    carrito_print = ""

    print(f"""
    Bienvnido al carrito mas fachero del mundo mundial.

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
        modo_de_busqueda=fun_car.op1(inventario,modo_de_busqueda,menu)

    elif op == "2":
        modo_de_busqueda=fun_car.op2(inventario,modo_de_busqueda,carrito,menu)



    else:
        print("Opcion no valida. Precione cualquier tecla para continuar")
        op=input(": ")
        os.system("cls")
