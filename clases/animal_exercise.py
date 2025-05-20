""" Clase Animal con Métodos de Acción Diseña una clase Animal con atributos especie y sonido.
    Agrega un método hacer_sonido() que imprima el sonido del animal. """


class Animal:
    def __init__(self, especie: str, sonido: str):
        self.especie = especie
        self.sonido = sonido
    
    def hacer_sonido(self):
        return f'El {self.especie} hace {self.sonido}'


perro = Animal('Perro', 'Guaooo')
gato = Animal('Gato', 'Miauu')
print(perro.hacer_sonido())
print(gato.hacer_sonido())