# Archivo: asociacion.py

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def estudiar(self, materia):
        print(f"{self.nombre} está estudiando {materia}")

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def enseñar(self, materia):
        print(f"{self.nombre} está enseñando {materia}")

# Uso de la asociación
estudiante1 = Estudiante("Diiego")
profesor1 = Profesor("Dra. Vanessa")

estudiante1.estudiar("Matemáticas")
profesor1.enseñar("Matemáticas")
