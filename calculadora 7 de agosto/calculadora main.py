from caculadora_funciones import *
import os

op = 0
resultado = 0
escrito = ""
estado = 0
operador = ["sumar","restar","multiplicar","dividir","potenciar","radicar"]
simbolo = ["+","-","x","/"]


def cls():
    os.system("cls")

def wait():
    wait = input("Presione ENTER para continuar")


while True:
    cls()

    flag = True

    while flag == True:
        cls()

        print(escrito)

        if len(escrito) == 0:
            print("Bienvenido a la calculadora de Eleazar\nIngrese un numero para comenzar.")
        else:
            print(f"\nIngrese un numero por el cual {operador[estado]} al anterior.")

        num = input(":  ")
        num = (verificar(num))

        cls()

        if num == "error":
            print("Por favor ingrese un numero valido. Enteros, decimales o fracciones.")
            wait()
        
        elif (num == 0) and (estado == 3):
            print("error. No se puede dividir por 0. Ingrese otro numero.")
            wait()

        elif (num % 2 == 0) and (estado == 5) and (resultado < 0):
            print("Error. Radicar un numero negativo por un numero positivo da un resultado imaginario. Ingrese otro numero")
            wait()
        
        else:
            if len(escrito) == 0:
                resultado = num
            else:
                match estado:
                    case 0:
                        resultado = sumar(resultado,num)
                    case 1:
                        resultado = restar(resultado,num)
                    case 2:
                        resultado = multiplicar(resultado,num)
                    case 3:
                        resultado = dividir(resultado,num)
                    case 4:
                        resultado = potenciar(resultado,num)
                    case 5:
                        resultado = radicar(resultado,num)
            if (estado != 5) and (estado != 4):
                if num < 0:
                    num = "(" + str(num) + ")"
                escrito += " " + str(num)

            elif estado == 4:
                escrito = "(" + escrito + " )^" + str(num)

            elif estado == 5:
                escrito = "(" + str(num) + "√"+ escrito + " )" 
            flag = False

    ########

    flag = True
    while flag == True:
        cls()

        print(escrito)

        print(f"\nResultado : {resultado}")

        print("""
    Ingrese una operación:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Potenciar
    6) Radicar
    0) Borrar todo
            """)

        op = input(":  ")
        op.lower()

        cls()

        if op not in ["1","2","3","4","5","6","0"]:
            print("La opción ingresada no es valida.")
            wait()

        else:
            if op == "0":
                escrito = ""
                resultado = 0
                estado = 0
            else:
                estado = int(op) - 1
                if estado < 4:
                    escrito += " " + simbolo[estado]

            flag = False