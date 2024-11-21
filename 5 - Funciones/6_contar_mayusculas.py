'''
Ejercicio 6. 
Escribir una función que pida una cadena de caracteres y que devuelva cuántos de 
ellos son mayúsculas.

'''

# Función que cuenta cuántos caracteres son mayúsculas en una cadena
def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

# Solicitar una cadena al usuario
cadena = input("Introduce una cadena de caracteres: ")

# Contar y mostrar las mayúsculas
print(f"El número de mayúsculas en la cadena es: {contar_mayusculas(cadena)}.")

# Función que cuenta cuántos caracteres son mayúsculas en una cadena
def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

# Solicitar una cadena al usuario
cadena = input("Introduce una cadena de caracteres: ")

# Contar y mostrar las mayúsculas
print(f"El número de mayúsculas en la cadena es: {contar_mayusculas(cadena)}.")
