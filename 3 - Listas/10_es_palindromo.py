# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# Comprobar si la palabra es un palíndromo
if palabra.lower() == palabra.lower()[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
