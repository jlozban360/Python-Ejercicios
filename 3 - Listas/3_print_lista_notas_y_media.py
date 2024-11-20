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
