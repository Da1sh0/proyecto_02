# Archivo: composicion.py

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("Gasolina")

# Uso de la composición
coche1 = Coche("Toyota")

print(f"{coche1.marca} tiene un motor de tipo {coche1.motor.tipo}")
