'''
Ejercicio 1. 
Escribir una función que determine si una letra dada es consonante. 

'''

# Función que determina si una letra es consonante
def es_consonante(letra):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    
    # Comprobar si la letra es una consonante
    if letra.isalpha() and letra not in vocales:
        return True
    return False

# Solicitar al usuario una letra
letra = input("Introduce una letra: ")

# Verificar si es consonante
if es_consonante(letra):
    print(f"{letra} es una consonante.")
else:
    print(f"{letra} no es una consonante.")
