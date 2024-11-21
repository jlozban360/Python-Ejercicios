'''
Ejercicio 2. 
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte 
al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de 
kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

'''

# Crear un diccionario con los precios de las frutas
precios_frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Preguntar por la fruta y los kilos
fruta = input("Introduce la fruta: ").capitalize()
kilos = float(input("Introduce el número de kilos: "))

# Verificar si la fruta está en el diccionario y calcular el precio
if fruta in precios_frutas:
    precio = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {precio}€.")
else:
    print("La fruta no está en el diccionario.")
