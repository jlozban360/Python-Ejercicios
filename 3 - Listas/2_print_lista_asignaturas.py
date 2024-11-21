'''
Ejercicio 2. 
Escribir un programa en Python que almacene las asignaturas de un curso (por 
ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre 
por pantalla el mensaje “Yo estudio <asignatura>”, donde <asignatura> es cada una 
de la de la lista. 

'''

# Almacenar asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar el mensaje para cada asignatura
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")
