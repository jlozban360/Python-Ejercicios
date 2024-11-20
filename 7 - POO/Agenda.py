class Agenda:
    def __init__(self):
        self.contactos = {}

    def añadir_contacto(self):
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        self.contactos[nombre] = {'teléfono': telefono, 'email': email}
        print(f"Contacto {nombre} añadido.")

    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for nombre, datos in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {datos['teléfono']}, Email: {datos['email']}")

    def buscar_contacto(self):
        nombre = input("Introduce el nombre del contacto a buscar: ")
        if nombre in self.contactos:
            datos = self.contactos[nombre]
            print(f"Contacto encontrado - Nombre: {nombre}, Teléfono: {datos['teléfono']}, Email: {datos['email']}")
        else:
            print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Introduce el nombre del contacto a editar: ")
        if nombre in self.contactos:
            telefono = input("Introduce el nuevo teléfono: ")
            email = input("Introduce el nuevo email: ")
            self.contactos[nombre] = {'teléfono': telefono, 'email': email}
            print(f"Contacto {nombre} actualizado.")
        else:
            print("Contacto no encontrado.")

    def cerrar_agenda(self):
        print("Agenda cerrada.")
        exit()

    def menu(self):
        while True:
            print("\nMenú de la agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.lista_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                self.cerrar_agenda()
            else:
                print("Opción no válida.")

# Crear la instancia y ejecutar el menú
agenda = Agenda()
agenda.menu()
