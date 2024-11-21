'''
Ejercicio 1
Escribe un programa que pida un número y después nos informe si el número es divisible por 2, 
de no ser así compruebe si es divisible por 3 e informe y si tampoco es así, si es divisible
por 5 e informe.

'''

# Pedir número por teclado para ver si es divisible entre dos,m 
try:
    numeroIntroducido = int(input("Introduce un número: "))

    # Elseif
    if numeroIntroducido % 2 == 0:
        print("Es divisible entre dos.")
    elif numeroIntroducido % 3 == 0:
        print("Es divisible entre tres.")
    elif numeroIntroducido % 5 == 0:
        print("Es divisible entre cinco.")
    else:
        print("No es divisible entre dos ni tres ni cinco.")
except ValueError:
    print("Por favor, introduce un número válido.")