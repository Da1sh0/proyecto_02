# Archivo: asociacion_dirigida.py

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        print(f"{self.nombre} está trabajando")

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre

    def asignar_empleado(self, empleado):
        print(f"{self.nombre} ha asignado a {empleado.nombre} al proyecto")

# Uso de la asociación dirigida
empleado1 = Empleado("Diiego")
proyecto1 = Proyecto("Proyecto_software_contable")

proyecto1.asignar_empleado(empleado1)
