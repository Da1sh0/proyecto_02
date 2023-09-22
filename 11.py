class MiClase:
    # Atributo estático
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        # Incrementar el contador cada vez que se crea una instancia
        MiClase.contador += 1

    # Método estático para obtener el valor actual del contador
    @staticmethod
    def obtener_contador():
        return MiClase.contador

    # Método de instancia para saludar
    def saludar(self):
        return f"Hola, soy {self.nombre}."

# Crear instancias de la clase
objeto1 = MiClase("Objeto1")
objeto2 = MiClase("Objeto2")

# Acceder al atributo estático desde la clase
print("Contador desde la clase:", MiClase.contador)

# Acceder al atributo estático desde una instancia
print("Contador desde la instancia (objeto1):", objeto1.contador)

# Usar el método estático para obtener el contador
print("Contador usando el método estático:", MiClase.obtener_contador())

# Llamar al método de instancia
print(objeto1.saludar())
print(objeto2.saludar())
