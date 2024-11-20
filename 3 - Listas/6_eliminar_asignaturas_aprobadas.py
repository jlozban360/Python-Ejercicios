# Almacenar asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

# Pedir la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)

# Eliminar asignaturas aprobadas (nota >= 5)
for i in range(len(asignaturas)-1, -1, -1):
    if notas[i] >= 5:
        asignaturas.pop(i)

# Mostrar las asignaturas que hay que repetir
print("Las asignaturas que tienes que repetir son:", asignaturas)
