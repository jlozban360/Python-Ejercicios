# Solicitar el verbo en infinitivo
verbo = input("Introduce un verbo regular en infinitivo (terminado en -ar): ")

# Eliminar la terminación -ar para obtener la raíz
raiz = verbo[:-2]

# Conjugaciones en presente de indicativo
print(f"Yo {raiz}o")
print(f"Tú {raiz}as")
print(f"Él/Ella {raiz}a")
print(f"Nosotros {raiz}amos")
print(f"Vosotros {raiz}áis")
print(f"Ellos/Ellas {raiz}an")
