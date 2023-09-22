class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado

    # Setter para el atributo 'nombre'
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para el atributo 'nombre'
    def get_nombre(self):
        return self.__nombre

    # Setter para el atributo 'precio'
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

    # Getter para el atributo 'precio'
    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto("Camiseta", 20.0)
    print(producto1)
    producto1.set_precio(25.0)
    print("Nuevo precio:", producto1.get_precio())
