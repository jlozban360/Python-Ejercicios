'''
Ejercicio 1.  
Escribir un algoritmo que, para cualquier número de segundos inferior a un millón, 
calcule su equivalente en días, horas, minutos y segundos. 
En este ejercicio tenemos que tener en cuenta que: 

1 minuto = 60 segundos. 
1 hora = 60 minutos = 3600 segundos. 
1 dia = 24 horas = 1440 minutos = 86400 segundos.

'''

# Solicitar el número de segundos
segundos = int(input("Introduce el número de segundos (menos de un millón): "))

# Comprobar que el número de segundos sea menor a un millón
if segundos >= 1000000:
    print("El número de segundos debe ser inferior a un millón.")
else:
    # Calcular los días, horas, minutos y segundos
    dias = segundos // 86400
    segundos = segundos % 86400
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60

    # Mostrar el resultado
    print(f"{dias} días, {horas} horas, {minutos} minutos, {segundos} segundos.")
