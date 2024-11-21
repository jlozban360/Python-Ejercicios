'''
Ejercicio 7
Haremos un programa que estará pidiendo números pares indefinidamente hasta que se introduzca un número impar.
El programa finalizará cuando se introduzca el primer número impar.

'''

while True:
    numero = int(input("Introduce un número par: "))
    if numero % 2 != 0:  # Si el número es impar, terminamos
        print("¡Has introducido un número impar! Fin del programa.")
        break
    print("Número correcto, sigue introduciendo...")
