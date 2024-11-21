'''
Ejercicio 3. 
0.70 
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes. 

'''

# Diccionario con los nombres de los meses
meses = {
    "01": "enero", "02": "febrero", "03": "marzo", "04": "abril",
    "05": "mayo", "06": "junio", "07": "julio", "08": "agosto",
    "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
}

# Pedir una fecha en formato dd/mm/aaaa
fecha = input("Introduce una fecha (dd/mm/aaaa): ")

# Dividir la fecha usando split y formatear el mensaje
dia, mes, año = fecha.split("/")
print(f"{dia} de {meses[mes]} de {año}")
