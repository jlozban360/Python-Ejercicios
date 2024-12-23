'''
Ejercicio 7. 
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. 

'''

# Almacenar el abecedario en una lista
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Eliminar las letras en posiciones múltiples de 3 (índices 3, 6, 9...)
abecedario = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

# Mostrar la lista resultante
print("El abecedario sin las letras en posiciones múltiples de 3:", abecedario)
