'''
Ejercicio 4. 
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés 
separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las 
palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.

'''

# Crear un diccionario de traducción
traducciones = {}

# Pedir al usuario las palabras y sus traducciones
entradas = input("Introduce las palabras y sus traducciones (separadas por comas): ").split(",")
for entrada in entradas:
    palabra, traduccion = entrada.split(":")
    traducciones[palabra.strip()] = traduccion.strip()

# Pedir una frase en español para traducir
frase = input("Introduce una frase en español: ")

# Traducir palabra por palabra
frase_traducida = []
for palabra in frase.split():
    frase_traducida.append(traducciones.get(palabra, palabra))  # Si no está en el diccionario, la dejamos igual

# Mostrar la frase traducida
print("Frase traducida:", " ".join(frase_traducida))
