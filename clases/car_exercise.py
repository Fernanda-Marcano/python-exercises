class Car:
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'


car1 = Car('Ford', 'Ford Fiesta', 'Negro')

print(car1.print_data())