class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia de la clase Persona
persona = Persona("Vanessa", 18)

# Agregar un atributo al vuelo llamado 'ciudad'
persona.ciudad = "Bogotá"

# Acceder a los atributos
print("Nombre:", persona.nombre)
print("Edad:", persona.edad)
print("Ciudad:", persona.ciudad)
