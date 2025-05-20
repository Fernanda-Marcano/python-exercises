""" Clase Producto con Descuento Implementa una clase Producto con 
    atributos nombre, precio y descuento. Agrega un método calcular_precio_final() 
    que aplique el descuento al precio del producto. """

class Product:
    def __init__(self, nombre: str, precio: float, descuento: int):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
    
    def calcular_precio_final(self):
        calcular_desc = (self.precio * self.descuento)/100
        precio_final = self.precio - calcular_desc
        return f'El precio del producto con descuento es: {precio_final}$'

product1 = Product('telefono', 240.40, 20)
print(product1.calcular_precio_final())