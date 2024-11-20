# Clase padre Cuenta
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir_datos(self):
        print(f"Titular: {self.titular}, Saldo: {self.cantidad}")


# Clase hija CajaAhorro
class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        print(f"Caja de Ahorro - Titular: {self.titular}, Saldo: {self.cantidad}")


# Clase hija PlazoFijo
class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        interes = self.obtener_interes()
        total = self.cantidad + interes
        print(f"Plazo Fijo - Titular: {self.titular}, Plazo: {self.plazo} meses, Interés: {self.interes}%, Total con interés: {total}")


# Crear instancias de cada clase
cuenta_ahorro = CajaAhorro("Juan", 1000)
plazo_fijo = PlazoFijo("Ana", 2000, 12, 5)

# Mostrar la información
cuenta_ahorro.mostrar_informacion()
plazo_fijo.mostrar_informacion()