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
