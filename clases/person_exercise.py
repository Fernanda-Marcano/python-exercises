""" Definir una Clase Persona: Crea una clase Persona con atributos nombre, 
    edad y nacionalidad. Implementa un método presentarse() que muestre un 
    mensaje con la información de la persona. """

class Person:
    def __init__(self, name: str, age: int, nationality: str):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    def introduce_yourself(self):
        text = f'''My name is {self.name}, I'm {self.age} years and I'm from {self.nationality}'''
        return text

person1 = Person('Fernanda', 24, 'Venezuela')
print(person1.introduce_yourself())
