# Definición de las clases base
class Mamifero:
    def comer(self):
        print("El mamífero come alimentos sólidos")

class Ave:
    def comer(self):
        print("El ave come granos y gusanos")

# Clase que hereda de ambas clases base
class Murcielago(Mamifero, Ave):
    def volar(self):
        print("El murciélago puede volar")

# Crear una instancia de la clase Murcielago
murcielago = Murcielago()

# Llamar al método 'comer' de la clase Murcielago
murcielago.comer()  # El resultado depende del orden de herencia, en este caso, se usará el de Mamifero

# Llamar al método 'volar' de la clase Murcielago
murcielago.volar()
