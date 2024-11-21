'''
Ejercicio 10. 
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un 
palíndromo.

'''

# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# Comprobar si la palabra es un palíndromo
if palabra.lower() == palabra.lower()[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
