'''
Ejercicio 6. 
Desarrollar un módulo que solicite al usuario el ingreso de un nombre de usuario y con
traseña y que los valide utilizando los módulos generados en los dos ejercicios anterio
res. Ayuda: para contar la cantidad de caracteres de una cadena, en Python se utiliza la 
función incorporada: len(cadena).

'''

from validar_usuario import validar_usuario
from validar_contrasenia import validar_contrasenia

def validar_usuario_y_contraseña():
    usuario = input("Introduce un nombre de usuario: ")
    validacion_usuario = validar_usuario(usuario)
    if validacion_usuario != True:
        print(validacion_usuario)
        return
    
    contraseña = input("Introduce una contraseña: ")
    validacion_contraseña = validar_contrasenia(contraseña)
    if validacion_contraseña != True:
        print(validacion_contraseña)
        return
    
    print("Usuario y contraseña válidos.")

# Ejecutar validación
validar_usuario_y_contraseña()
