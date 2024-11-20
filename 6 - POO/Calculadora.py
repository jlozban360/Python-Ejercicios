# Definir la clase Calculadora
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir entre 0."

# Solicitar los valores a calcular
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
calculadora = Calculadora(num1, num2)

# Realizar las operaciones y mostrar los resultados
print(f"Suma: {calculadora.suma()}")
print(f"Resta: {calculadora.resta()}")
print(f"Multiplicación: {calculadora.multiplicacion()}")
print(f"División: {calculadora.division()}")
