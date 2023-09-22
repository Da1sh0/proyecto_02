from abc import ABC, abstractmethod

# Definir una "interfaz" llamada FormaGeometrica
class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Clase concreta que implementa la interfaz FormaGeometrica
class Rectangulo(FormaGeometrica):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Clase concreta que implementa la interfaz FormaGeometrica
class Circulo(FormaGeometrica):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159265359 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.14159265359 * self.radio

# Intentar crear una instancia de FormaGeometrica (esto generará un error)
# forma = FormaGeometrica()

# Crear instancias de Rectangulo y Circulo
rectangulo = Rectangulo(4, 5)
circulo = Circulo(3)

# Calcular y mostrar áreas y perímetros
print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())

print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())
