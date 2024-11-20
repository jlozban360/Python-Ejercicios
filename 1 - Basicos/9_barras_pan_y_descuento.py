# Precio y descuento
precio_barra = 0.69
descuento = 0.60

# Pedir el número de barras no frescas vendidas
barras_no_frescas = int(input("¿Cuántas barras de pan no frescas se han vendido? "))

# Calcular precios
precio_habitual = barras_no_frescas * precio_barra
descuento_total = precio_habitual * descuento
coste_final = precio_habitual - descuento_total

# Mostrar los resultados
print(f"Precio habitual de una barra: {precio_barra}€")
print(f"Descuento total aplicado: {descuento_total:.2f}€")
print(f"Coste final: {coste_final:.2f}€")