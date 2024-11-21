'''
Ejercicio 2
Escribe un programa que nos pida el nombre del usuario y compruebe la longitud en caracteres del nombre introducido. 
Nos dirá si el nombre es largo o se trata de un nombre corto y además en el caso de que el nombre sea largo, 
nos debe decir si el nombre es compuesto o no. 

Suma = n (n + 1) / 2

'''

# Pedir al usuario un número entero
n = int(input("Introduce un número entero: "))

# Calcular la suma usando la fórmula Suma = n(n + 1) / 2
suma = n * (n + 1) // 2  # Usamos // para que la división sea entera

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")