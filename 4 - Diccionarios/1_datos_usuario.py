'''
Ejercicio 1. 
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde 
en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>. 

'''

# Crear un diccionario para almacenar los datos
usuario = {}

# Preguntar al usuario por sus datos
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = int(input("Introduce tu edad: "))
usuario['direccion'] = input("Introduce tu dirección: ")
usuario['telefono'] = input("Introduce tu número de teléfono: ")

# Mostrar el mensaje con los datos
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
