'''
Ejercicio 1.  
 
Realizar un programa que conste de una clase llamada Alumno que tenga como atribu
tos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. 

'''

# Definir la clase Alumno
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")

# Crear una instancia de la clase Alumno
nombre = input("Introduce el nombre del alumno: ")
nota = float(input("Introduce la nota del alumno: "))
alumno = Alumno(nombre, nota)

# Mostrar los datos e indicar si ha aprobado o no
alumno.imprimir_datos()
alumno.resultado()
