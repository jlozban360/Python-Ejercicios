'''
Ejercicio 9. 
Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
número de veces que contiene cada vocal.

'''

# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# Inicializar el contador de vocales
vocales = "aeiou"
conteo = {vocal: palabra.lower().count(vocal) for vocal in vocales}

# Mostrar el número de veces que aparece cada vocal
for vocal, cantidad in conteo.items():
    print(f"La vocal {vocal} aparece {cantidad} veces.")
