# Archivo: agregacion.py

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

# Uso de la agregación
departamento1 = Departamento("Recursos Humanos")
empleado1 = Empleado("Vanessa", departamento1)

print(f"{empleado1.nombre} trabaja en el departamento de {empleado1.departamento.nombre}")
