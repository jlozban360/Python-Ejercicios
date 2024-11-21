'''
Ejercicio 2
Escribe un programa que nos pida el nombre del usuario y compruebe la longitud en caracteres del nombre introducido. 
Nos dirá si el nombre es largo o se trata de un nombre corto y además en el caso de que el nombre sea largo, nos debe 
decir si el nombre es compuesto o no.

'''

# Pedimos al usuario que introduzca su nombre
nombre = input("Introduce tu nombre: ")

# Comprobamos la longitud del nombre
longitud = len(nombre)  # Calculamos el número de caracteres del nombre

# Si el nombre tiene más de 10 caracteres, lo consideramos largo
if longitud > 10:
    print("Tienes un nombre largo.")
    
    # Comprobamos si el nombre es compuesto (si contiene un espacio)
    if " " in nombre:
        print("Tu nombre es largo y también compuesto.")
    else:
        print("Tu nombre es largo pero no es compuesto.")
# Si el nombre tiene 10 o menos caracteres, lo consideramos corto
else:
    print("Tienes un nombre corto.")
