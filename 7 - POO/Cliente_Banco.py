'''
Ejercicio 2. 
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El 
banco requiere también al final del día calcular la cantidad de dinero que se ha deposi
tado. 
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los 
atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. 
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos 
__init__, operar y deposito_total.

'''

class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, cantidad):
        self.cantidad += cantidad
        print(f"{self.nombre} ha depositado {cantidad}. Nuevo saldo: {self.cantidad}")

    def extraer(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"{self.nombre} ha extraído {cantidad}. Nuevo saldo: {self.cantidad}")
        else:
            print("Saldo insuficiente.")

    def mostrar_total(self):
        print(f"Saldo de {self.nombre}: {self.cantidad}")


class Banco:
    def __init__(self, cliente1, cliente2, cliente3):
        self.clientes = [cliente1, cliente2, cliente3]
        self.total_depositado = 0

    def operar(self):
        for cliente in self.clientes:
            cliente.mostrar_total()

    def deposito_total(self):
        for cliente in self.clientes:
            self.total_depositado += cliente.cantidad
        print(f"Total depositado en el banco: {self.total_depositado}")


# Crear instancias de clientes
cliente1 = Cliente("Carlos", 500)
cliente2 = Cliente("Ana", 1000)
cliente3 = Cliente("Pedro", 1500)

# Crear instancia del banco
banco = Banco(cliente1, cliente2, cliente3)

# Realizar operaciones
banco.operar()
banco.deposito_total()
