

# ASI SE HACE UN COMENTARIO.


### ASI TAMBIEN. CUANTAS "#" COMO QUIERAS.

'''

Comentario multilinea.

Puedes escribir muchas cosas.

'''

variable_string = "string" #String significa cadena. Es una cadena de texto.

variable_int = 0 #int significa entero. Es un numero sin coma o punto.

variable_float = 0,5 #Float significa decimal. Un numero con numeros despues de la coma o punto.

variable_boolean = True #Bool es una variable que solo puede tener dos estados True o False. True y False se escriben con la primera letra en mayuscula.

ejemplo = input("") #Input significa ingreso. recibe valores que el usuario ingresa por teclado. En este caso, la variable ejemplo recibe un valor.

print (ejemplo) #Print = imprime por consola el valor que previamente hayas almacenado en una variable. En este caso, imprime el valor ingresado previamente en la variable ejemplo.

ejemplo = input("ingresa un valor:  ") #Puedes escribir dentro de los parentesis del input. El usuario vera lo que escribiste antes de ingresar un valor.

type(ejemplo) #Type se utiliza para saber que tipo de valor contiene una variable. En este caso vamos a descubrir que tipo de dato es la variable ejemplo.

len(ejemplo) #Se utiliza para conocer la longitud de una variable o una lista

'''
Puedes utilizar los parentesis para espeficicar que hace tu codigo de manera compleja.
En este caso le vamos a deir al programa que:
'''
# IMPRIME: (que tipo de dato es (ejemplo))

print(type(ejemplo))

'''
El dibujo de una casa no es lo mismo que una casa.
Igual pasa con los numeros: el valor de un numero no es lo mismo que el simbolo con lo que lo representamos.
Todos los datos que ingresas por consola son texto (string), sin importar si ingresas un numero.
'''

ejemplo = int(input(""))

'''
Cuando utilizas int() estas convirtiendo algo en un numero entero. Esto puede dar errores, pero si quieres usar operaciones matmaticas, vas a tener que usarlo.

'''

numero_entero = int(input("Ingresa un numero entero por favor:  "))
otro_numero_entero = int(input("Ingresa otro numero entero por favor"))

suma = numero_entero + otro_numero_entero

print (suma) # Asi se suma.

'''
suma +
resta -
multiplicacion *
division /
potencia **
'''

'''
Tambien podemos convertir variables a otros tipos, simplemente ingresando el tipo de dato al que lo queremos convertir, seguido de la variable que queremos convertir entre parentesis.

str(variable) texto, cadenas, string
int(variable) numero entero, int
float(variable) numero con decimal, float
'''

while ():
    ejemplo = "ejemplo nunca cambiara, porque el bucle no se ejecuta"

# while es un bucle. Se repite todo lo que esta dentro de el, mientra se cumpla la condicion dentro de los parentesis.
# El while anterior no va a hacer nada, pues esta vacio en su condicion, pero el siguiente se ejecuta por siempre.





while (1):
    ejemplo = 0

# Ten cuidado de no hacer bucles infinitos como el anterior. puedes crear contadores para decidir cuando termina un bucle.





contador = 0 # Primero inicializamos contador como un numero 0

while ( contador < 10):
    contador = contador + 1
# El bucle anterior se repetira hasta que contador sea igual a 10, terminando con el bucle.





if (): #Esto es una condicion If. Si se cumple la condicion, entonces se va a ejecutar lo que esta adentro. Si no, no.
    ejemplo = 0





if ():
    ejemplo = 0
else:   #Esto es un else. Si la condicion no se cumple, lo que esta dentro del else se va a cumplir.
    ejemplo = 2





if ():
    ejemplo = 0
elif (1):
    ejemplo = 1
elif (2):
    ejemplo = 2
else:
    ejemplo =4

'''

El anterior if tambien contiene un elif
El elif es una segunda condificion que se ejecuta cuando la condificion del if falla.
A diferencia del else, no se ejecuta siempre que el if falla, sino solo cuando otra condicion tambien se cumple.

'''

for repeticion in range(): #For es un bucle que se repite una cantidad exacta de veces. Cada repeticion tiene un nombre. En este caso se llama repeticion.
    ejemplo = 0
'''
por cada repeticion en el rango de (0 hasta 10):
    haz algo, en este caso: ejemplo tendra el valor de 0
'''






for repeticion in range ( 0 , 10 ):
    ejemplo = 0 + repeticion

# en el ejemplo anterior, el programa se repite 10 veces y en cada repeticion, ejemplo sera igual a 0 + el numero de veces que se va repitiendo el for
'''

Algo importante que tener en cuenta sobre los while y for:
la primera repeticion sera la numero 0, y si pasa por 10 repeticiones, entonces terminara en la repeticion 9

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

'''

# La variable dentro del for es local, osea que no se utiliza fuera del for. Esta misma puede tener cualquier nombre. Usualmente se utiliza i

for i in range( 0 , 10):
    ejemplo = i

lista = []





# Una lista es una serie de variables dentro de una sola.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_cadenas = ["hola" , "adios" , "pollosaurio"]





lista_de_numeros[3]
# Cuando pones un numero entre los corchetes, estas refiriendote al elemento que ocupa esa posicion en la lista. Por ejemplo; en la lista anterior, el elmento que ocupa el tercer lugar es el numero 4






lista.append(0) # Utiliza append para agregar un valor a una lista, como el ultimo elemento de esta.
lista.pop(0) # Elimina un elemento de la lista, en la posicion que ingresemos
lista.remove(0) # Elimina un elemento de la lista que sea igual al que ingresamos
#muchas otros metodos para funciones se pueden encontrar aqui  https://www.w3schools.com/python/python_ref_list.asp

# Puedes utilizar un for para recorrer una lista

for i in range (0, len(lista)): #Utilizamos len para conocer la longitud de la lista y no pasarnos de largo.
    ejemplo = lista[i]

'''
i cambia de valor en cada repeticion del for.
Al usar lista[i], le estamos diciendo al programa que busque el valor que se encuentra dentro de una posicion. La posicion del numero que i tenga como valor
finalmente, el valor dentro de la lista, en la posicion de i, es guardado dentro de la variable ejemplo

ejemplo es igual a un elemento de la lista, dentro de la posicion numero i
ejemplo      =                       lista [                             i  ]
'''

# Para armar una matriz

lista = []
filas = 5
columnas = 5
for i in range (0,filas):
    lista.append([0]*columnas)

# Para imprimir una matriz

msj = ""
for i in range (0,len(lista)):
    for k in range (0,len(lista[i])):
        msj += f" {lista[i][k]} -"
    msj += "\n"

print (msj)