"""
Ejercicio2:
Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos.
"""

import math
import os

while 1:

    os.system("cls")
    lista =  input("Por favor, ingrese una lista de numeros enteros o decimales separados por esapcios: ")

    lista = lista.split()

    con = 0

    if len(lista) > 0:
    
        try:

            for num in lista:

                decim = False

                for letra in num:
                    
                    if (letra == ".") or (letra == ","):
                        decim = True
                
                if decim == True:
                    numero = float(num.replace("," , "."))
                else:
                    numero = int(num)

                lista[con] = numero

                con += 1


            menor = lista[0]
            mayor = lista[0]

            con = 0
            suma = 0
            msj = ""

            for num in lista:
                if num > mayor:
                    mayor = num
                if num < menor:
                    menor = num

                con += 1
                suma += num
                
                
                msj += str(num)

                if con != len(lista):
                    msj += " , "

            suma = round(suma , 10)
            promedio = suma / con
            variansa = 0
            equis = 0

            for num in lista:

                resta = num - promedio

                equis = equis + round(resta**2 , 10)
            
            variansa = round(equis / con , 10)
            desviacion = math.sqrt(variansa)

            print (f"""

        De la siguiente lista de numeros:

        {msj}

        La suma de los numeros es igual a {suma}
        El promedio es de {promedio}

        El mayor es {mayor}
        El menor es {menor}

        La variansa es igual a {variansa} y la desviacion estandar es igual a {desviacion}
        """)

            space = input("\n:    ")

        except ValueError:
            print ("Disculpe. Debe ingresar una lista valida. Numeros enteros o decimales, separados por esapcios. Sin letras o simbolos")

            space = input("\n:     ")