""" Clase Producto: 
    - Implementar una clase producto con atributos como (nombre, precio, id). 
    Integrar los métodos mágicos __repr__, __str__ y __add__"""

class Product:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
    
    def __add__(self, other):
        if isinstance(other, Product):
            total_precio = self.precio + other.precio
        return f'El total: {total_precio}'
    
    def __repr__(self):
        return f'Product({self.nombre}, {self.precio})'
    
    def __str__(self):
        return f'\nNombre del Producto: {self.nombre}\nPrecio del Producto: {self.precio}\n'

producto1 = Product("Teléfono", 500)
producto2 = Product("Audífonos", 100)

print(producto1 + producto2)
print(producto1)
print(producto2)