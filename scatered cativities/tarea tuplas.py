import os


######
"""
Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
error.
El programa termina cuando el usuario introduce un cero.
"""
######


def tuplas_meses():
    tupla_meses = ( "" , "enero" , "febrero" ,"marzo", "abril", "mayo" , "junio" , "julio" , "agosto" , "septiembre" , "octubre" , "noviembre" , "diciembre" )

    while 1:

        num=int(input("ingrese un numero correspondiente a un mes:   "))

        if num == 0:
            os.system("cls")
            op = input("\nprograma terminado. Precione cualquier tecla para continuar:  ")
            break
        elif (num < 13) and (num > 0):
            for i in range(0,len(tupla_meses)):
                if i == num:
                    print (f"\n{tupla_meses[i]}\n")
        else:
            print ("\nvalor ingresado no es correcto\n")


######
"""
Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
repite según lo halle en la tupla que has creado.
RESUELVE validar los ingresos del usuario.
"""
######


def tupla_de_numeros():
    tupla_numeros = (1,1,4,4,4,2,3,3,3,3,5,5,6,7,7,7,7,8,8,9,9,9,9,9,10,11,12,12,12,12,12)

    while 1:
        con = 0
        try:
            num = int(input("Ingrese un numero mayor a 0 y menor a 13: "))
            if (num < 1) or (num > 12):
                print("numero fuera de tupla")
            else:
                print(f"El numero aparece {tupla_numeros.count(num)} vez en la tupla")
        except ValueError:
            print ("Lo que ingresaste no era un numero: ")


######
"""
Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.
"""
######


def tupla_mayor_menor():
    tupla_mayor = (23,67,32,34,56,78,90,120,101,44,89,13,66,99,34,41,57,71,22,79,104,134,20,21,119,118)
    mayor = tupla_mayor[0]
    menor = tupla_mayor[0]
    for i in tupla_mayor:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
    print(f"el numero menor de la tupla es {menor}, y el mayor es {mayor}")


######
"""
Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y
muestra los valores de la tupla.
RESUELVE el caso en que no exista ese índice en la tupla.
"""
######


def tupla_random():
    tupla_random = ("rana naranja","dinosaurio","el obelisco","mi padre en monopatin","russia","la virgen en aladelta","el quinto precidente de Bolivia","la final con Francia","una deuda millonaria","pollo a las brasas")

    while 1:
        num = int(input("Ingrese un indice para buscar oraciones random en una tupla:     "))

        if (num > -1) and (num < 10):
            print(tupla_random[num])
        else:
            print("valor ingresado fuera de rango")


######
"""
Escribe un programa que solicite al usuario que ingrese una lista de números enteros.
El programa debe crear una tupla a partir de la lista y luego imprimir la tupla en orden
inverso.
"""
######

def tupla_inversa():
    text = input("ingrese una lista de numeros enteros separados por coma o por espacios: ")
    
    text = text.replace(","," ")
    
    text = text.split()

    tupla = tuple(text)

    print(tupla)
    print(type(tupla))


######
"""
Escribe una función llamada intercambiar_tupla que acepte una tupla como parámetro
y devuelva una nueva tupla en la que el primer y el último elemento de la tupla
original se intercambian. Por ejemplo, si la tupla original es (1, 2, 3, 4), la función
debería devolver (4, 2, 3, 1).
"""
######


def intercambiar_tupla(tupla1):
    max = len(tupla1) - 1
    lista = list(tupla1)

    lista[max] = tupla1[0]
    lista[0] = tupla1[max]
    
    print(tuple(lista))


######
"""
Escribe una función llamada encontrar_pares_impares que acepte una tupla de
números enteros como parámetro y devuelva una tupla que contenga dos listas: una
lista de números pares y otra lista de números impares. Por ejemplo, si la tupla original
es (1, 2, 3, 4, 5, 6, 7, 8, 9), la función debería devolver ([2, 4, 6, 8], [1, 3, 5, 7, 9]).
"""
######


def encontrar_pares_impares(tupla1):
    par = []
    inpar = []

    for i in tupla1:
        if i % 2 == 0:
            par.append(i)
        else:
            inpar.append(i)

    print(f"""
Numeros pares: {par}
Numeros inpares: {inpar}
    """)


######
"""
Escribe un programa que solicite al usuario que ingrese una lista de nombres. El
programa debe crear una tupla a partir de la lista y luego imprimir los nombres que
comienzan con la letra 'A'.
"""
######


def filtrar_a (lista1):
    tupla = tuple(lista1)
    
    for i in tupla:
        if (i[0] == "A") or (i[0] == "a"):
            print(i)


######
"""
Escribe un programa que cree una tupla que contenga los primeros diez números de la
serie de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55) y luego imprima la tupla.
"""
######


def fibonacci ():
    num = 1
    tupla = [1,1]
    for i in range(0,8):
        
        num = tupla[len(tupla) - 1] + tupla[len(tupla) - 2]
        tupla.append(num)

    print( tuple(tupla) )


######
"""
Escribe un programa que reciba una tupla de colores y cree un diccionario donde cada
elemento de la tupla tenga una clave numérica incremental, empezando en 1. Imprime
la tupla de colores original y el diccionario resultante.
"""
######


def colores_dic (tupla1):

    dic = {}

    for i in range(0,len(tupla1)):
        dic[i+1] = tupla1[i]

    print(tupla1)
    print(dic)


######
"""
Dado el diccionario dic_edades que contiene como llave el nombre de una persona y
como valor su edad, escribe un programa que determine quién es la persona con
mayor edad y lo imprima por pantalla.
"""
######


def mayor_edad(dick): #dick stands for dictionary Key

    may = "primero"
    name = ""

    for i,k in dick.items():
        if may == "primero":
            may = k

        if k > may:
            may = k
            name = i
    
    print(f"""
La persona con mayor edad es {name}, con {may} años.
    """)


######
"""
Dado el diccionario dic_notas que contiene como llave el nombre de un estudiante y
como valor su nota en un examen, escribe un programa que calcule el promedio de notas y genere una lista con los nombres de los estudiantes que aprobaron (nota
mayor o igual a 7). Imprime por pantalla el promedio de notas y la lista de estudiantes
aprobados.
"""
######


def promedio_notas(dick1): #dick1 stands for dick 1

    nota = 0
    name = []

    for i,k in dick1.items():

        if k > 6:
            nota += k
            name.append(i)

    print("El promedio es igual a " + str( nota / len(dick1) ))
    msj = "Alumnos aprobados: "
    for i in range(0,len(name)):
        msj += name[i] + ", "
    print(msj)

