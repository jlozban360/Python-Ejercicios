# Definir la clase Triángulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triángulo equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("Es un triángulo isósceles.")
        else:
            print("Es un triángulo escaleno.")

# Solicitar los lados del triángulo
lado1 = float(input("Introduce el primer lado del triángulo: "))
lado2 = float(input("Introduce el segundo lado del triángulo: "))
lado3 = float(input("Introduce el tercer lado del triángulo: "))
triangulo = Triangulo(lado1, lado2, lado3)

# Mostrar el lado mayor y el tipo de triángulo
triangulo.lado_mayor()
triangulo.tipo_triangulo()
