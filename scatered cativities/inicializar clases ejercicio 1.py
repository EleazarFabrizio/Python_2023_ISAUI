# Enunciado:
# Crea una clase llamada "Rectangulo" que represente un rectángulo y 
# tenga los siguientes atributos:

# base: la longitud de la base del rectángulo.
# altura: la altura del rectángulo.

# La clase debe tener los siguientes métodos:

# calcular_area(): calcula y devuelve el área del rectángulo.
# calcular_perimetro(): calcula y devuelve el perímetro del rectángulo.

# A continuación, crea una instancia de la clase Rectangulo 
# con una base = 5 y una altura= 3. 
# Luego, muestra el área y el perímetro del rectángulo utilizando los métodos de la clase.

class rectangulo:

    def __init__(self , base , altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura)
        
    def calcular_perimetro(self):
        return ((self.base * 2) + (self.altura * 2))
        
    
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

rectangulito = rectangulo(base , altura)

area = rectangulito.calcular_area()
perimetro = rectangulito.calcular_perimetro()

print("El area del rectangulo es " + str(area))
print("El perimetro del rectangulo es " + str(perimetro))

