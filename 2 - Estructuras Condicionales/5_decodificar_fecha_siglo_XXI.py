'''
Ejercicio 5. 
Escribir un algoritmo que decodifique fechas del siglo XXI. El dato es un entero 
comprendido entre 10100 y 311299. El resultado es una secuencia de caracteres: 
número del día dentro del mes, del mes dentro del año y del año dentro del siglo. Por 
ejemplo, para el dato 30485, el resultado es el texto 3-4-2085. 

'''

# Solicitar la fecha en formato de 6 dígitos
fecha = int(input("Introduce una fecha en formato ddmmyy (ejemplo: 30485): "))

# Extraer día, mes y año
dia = fecha // 10000
mes = (fecha % 10000) // 100
anio = (fecha % 10000) % 100 + 2000  # Añadir 2000 para obtener el año completo

# Mostrar el resultado
print(f"La fecha es: {dia}-{mes}-{anio}")
