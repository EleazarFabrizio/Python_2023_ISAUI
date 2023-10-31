'''#para hacer una funcion con parametros predeterminados tiene que tener minimo un parametro definido 
def restar(num1=5, num2=2):
    return (num1 - num2)
print(restar())

#quiero que esta funcion me imprima una multiplicacion
def multi(num1=6, num2=3):
    return (num1 * num2)
print(multi(restar(7,1), 2))

#quiero que esta funcion me sume tareas a una lista
def tareas(hayTarea = "si" , tarea="no hay tarea"):
    lista=[]
    while (hayTarea == "si"):
        hayTarea = input("tiene mas tarea?")
        if (hayTarea == "si"):
            tarea=(input("ingrese una tarea:    "))
            lista.append(tarea)

    return lista

print(tareas())

#quiero que esta funcion me imprima un nombre, en el caso de no ingresar uno, me diga que es un nombre desconocido
def mi_nombre_es(identidad = "desconocido"):
    print ("mi nombre es " + identidad)

mi_nombre_es("Agos")

#quiero que esta funcion me imprima el clima de hoy 
def clima_de_hoy(text1="soleado", text2="templada"):
    print(f"Hoy es un dia {text1} con la temperatura {text2}")

clima_de_hoy("soleado","muy fria")

#quiero que esta funcion me imprima el clima del dia de hoy y de mañana
def clima(text1="soleado"):
    lista = []
    lista.append(f"hoy va a ser un dia {text1}")
    text1 = input("ingrese el clima de mañana:  ")
    lista.append(f"mañana va a ser un dia {text1}")
    print (lista)
clima()'''



def cosa_rara (datos = ["nombre","dni","telefono"]):
    salida = []
    for i in datos:
        salida.append(input(f"ingrese {i}:  "))

    return salida

print(cosa_rara(["apellido","nacionalidad","sexo"]))
