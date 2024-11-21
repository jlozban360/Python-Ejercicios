'''
Ejercicio 3. 
Escribir un algoritmo que, dado el infinitivo de un verbo regular de la primera 
conjugación, obtenga la conjugación en singular y plural de presente de indicativo. 
Por ejemplo, para el verbo cantar el resultado es yo canto, tú cantas, el canta, 
nosotros cantamos, vosotros cantáis, ellos cantan.

'''

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
