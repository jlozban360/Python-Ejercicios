'''
Ejercicio 8. 
Consideremos una hora expresada en forma de tripleta. Escribir un algoritmo que 
imprima la hora correspondiente al siguiente segundo. Por ejemplo, para la entrada 
13,43,24 tiene que devolver 13,43,25. 

'''

# Solicitar la hora en formato tripleta (hora, minuto, segundo)
hora, minuto, segundo = map(int, input("Introduce la hora (hora, minuto, segundo): ").split(','))

# Incrementar el segundo
segundo += 1

# Si el segundo llega a 60, incrementamos el minuto
if segundo == 60:
    segundo = 0
    minuto += 1

# Si el minuto llega a 60, incrementamos la hora
if minuto == 60:
    minuto = 0
    hora += 1

# Si la hora llega a 24, reiniciamos a 0 (nuevo día)
if hora == 24:
    hora = 0

# Mostrar la hora siguiente
print(f"La hora siguiente es: {hora:02}:{minuto:02}:{segundo:02}")
