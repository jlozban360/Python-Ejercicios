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
