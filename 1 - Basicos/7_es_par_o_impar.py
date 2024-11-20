while True:
    numero = int(input("Introduce un número par: "))
    if numero % 2 != 0:  # Si el número es impar, terminamos
        print("¡Has introducido un número impar! Fin del programa.")
        break
    print("Número correcto, sigue introduciendo...")
