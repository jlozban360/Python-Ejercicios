# Función para verificar si una frase es un palíndromo
def es_palindromo(frase):
    # Eliminar espacios y convertir a minúsculas
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

# Solicitar al usuario una frase
frase = input("Introduce una frase: ")

# Verificar si es un palíndromo
if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
