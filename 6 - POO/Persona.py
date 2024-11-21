'''
Ejercicio 3. 
 
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase 
con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño 
mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

'''

# Definir la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

# Crear una instancia de la clase Persona
nombre = input("Introduce el nombre de la persona: ")
edad = int(input("Introduce la edad de la persona: "))
persona = Persona(nombre, edad)

# Mostrar los datos e indicar si es mayor de edad
persona.mostrar_datos()
persona.es_mayor_de_edad()
