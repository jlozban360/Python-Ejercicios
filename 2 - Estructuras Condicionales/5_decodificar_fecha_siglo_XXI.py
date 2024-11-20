# Solicitar la fecha en formato de 6 dígitos
fecha = int(input("Introduce una fecha en formato ddmmyy (ejemplo: 30485): "))

# Extraer día, mes y año
dia = fecha // 10000
mes = (fecha % 10000) // 100
anio = (fecha % 10000) % 100 + 2000  # Añadir 2000 para obtener el año completo

# Mostrar el resultado
print(f"La fecha es: {dia}-{mes}-{anio}")
