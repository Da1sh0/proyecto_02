class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre  # Atributo privado
        self.__email = email    # Atributo privado

    # Setter para el atributo 'nombre'
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para el atributo 'nombre'
    def get_nombre(self):
        return self.__nombre

    # Setter para el atributo 'email'
    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    # Getter para el atributo 'email'
    def get_email(self):
        return self.__email

    def __str__(self):
        return f"Cliente: {self.__nombre}, Email: {self.__email}"

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", "juan@example.com")
    print(cliente1)
    cliente1.set_email("juan.perez@example.com")
    print("Nuevo email:", cliente1.get_email())
