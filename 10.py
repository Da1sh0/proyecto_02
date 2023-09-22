class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo privado
        self._edad = edad      # Atributo privado

    # Getter para el atributo 'nombre'
    def get_nombre(self):
        return self._nombre

    # Setter para el atributo 'nombre'
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    # Getter para el atributo 'edad'
    def get_edad(self):
        return self._edad

    # Setter para el atributo 'edad'
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Error: La edad no puede ser un número negativo.")

# Crear una instancia de la clase Persona
persona1 = Persona("Vanessa", 18)

# Obtener el nombre usando el getter
nombre_actual = persona1.get_nombre()
print("Nombre actual:", nombre_actual)

# Cambiar el nombre usando el setter
persona1.set_nombre("Diiego")
print("Nuevo nombre:", persona1.get_nombre())

# Intentar establecer un nombre no válido
persona1.set_nombre(90)  # Esto generará un mensaje de error

# Obtener la edad usando el getter
edad_actual = persona1.get_edad()
print("Edad actual:", edad_actual)

# Cambiar la edad usando el setter
persona1.set_edad(20)
print("Nueva edad:", persona1.get_edad())

# Intentar establecer una edad negativa
persona1.set_edad(-9)  # Esto generará un mensaje de error
