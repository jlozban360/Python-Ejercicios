'''
Ejercicio 4. 
Escribir un algoritmo que, para un número binario de 4 cifras, imprima su valor en 
base 10.  

'''

# Solicitar el número binario
binario = input("Introduce un número binario de 4 cifras: ")

# Convertir de binario a decimal
decimal = int(binario, 2)

# Mostrar el resultado
print(f"El número binario {binario} es igual a {decimal} en base 10.")
