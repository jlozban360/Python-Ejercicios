'''
Ejercicio 5
Vamos a hacer un programa que nos pida introducir números hasta que una entrada se deje vacía. El programa debe ir contando cuántos números se introducen y la suma de esos números.

'''

# Inicializar variables para contar y sumar
contador = 0
suma = 0

# Bucle para pedir números hasta que la entrada esté vacía
while True:
    entrada = input("Introduce un número (o deja vacío para terminar): ")
    if entrada == "":  # Salir si la entrada está vacía
        break
    numero = int(entrada)
    contador += 1
    suma += numero

# Mostrar el resultado
print(f"Has introducido {contador} números y su suma es {suma}.")
