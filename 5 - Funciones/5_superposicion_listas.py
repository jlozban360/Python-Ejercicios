# Función que verifica si dos listas tienen al menos un miembro en común
def superposicion(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

# Solicitar dos listas al usuario
lista1 = input("Introduce la primera lista (separada por comas): ").split(",")
lista2 = input("Introduce la segunda lista (separada por comas): ").split(",")

# Verificar la superposición
if superposicion(lista1, lista2):
    print("Las listas tienen al menos un miembro en común.")
else:
    print("Las listas no tienen miembros en común.")
