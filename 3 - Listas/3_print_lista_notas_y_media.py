'''
Ejercicio 3. 
Escribir un programa que almacene las asignaturas de un curso (por ejemplo, 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la 
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el 
mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las 
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
por el usuario. Finalmente, debe mostrar la nota media de todas las asignaturas.

'''

# Almacenar asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

# Pedir la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)

# Mostrar asignaturas con sus notas
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

# Calcular y mostrar la media de las notas
media = sum(notas) / len(notas)
print(f"La nota media es: {media}")
