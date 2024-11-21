'''
Ejercicio 5. 
Desarrollar un módulo para validación de contraseñas. Dicho módulo, deberá cumplir 
con los siguientes criterios de aceptación:  
• La contraseña debe contener un mínimo de 8 caracteres 
• Una contraseña debe contener letras minúsculas, mayúsculas, números y al me
nos 1 carácter no alfanumérico 
• La contraseña no puede contener espacios en blanco 
• Contraseña válida, retorna True 
• Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”

'''

import re

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "La contraseña debe contener al menos 8 caracteres"
    elif not re.search(r'[a-z]', contraseña):
        return "La contraseña debe contener al menos una letra minúscula"
    elif not re.search(r'[A-Z]', contraseña):
        return "La contraseña debe contener al menos una letra mayúscula"
    elif not re.search(r'[0-9]', contraseña):
        return "La contraseña debe contener al menos un número"
    elif not re.search(r'[^a-zA-Z0-9]', contraseña):
        return "La contraseña debe contener al menos un carácter no alfanumérico"
    elif " " in contraseña:
        return "La contraseña no puede contener espacios en blanco"
    else:
        return True

# Prueba de validación
contraseña = input("Introduce una contraseña: ")
resultado = validar_contraseña(contraseña)
print(resultado)
