""" Cuenta bancaria: 
	- Escribir una clase para simular una cuenta bancaria con métodos para depositar y retirar dinero. """

class Cuenta: 
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0
    
    def deposito(self, cantidad: int):
        if cantidad <= 0:
            return 'Error. La cantidad a depositar debe ser mayor a cero'
        self.saldo += cantidad
        return f'Usted ha depositado {cantidad}$ a su cuenta. Su saldo actual es: {self.saldo}'
    
    def retiro(self, cantidad: int):
        if cantidad <= 0:
            return 'Error. La cantidad a retirar debe ser mayor a cero'
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return f'Usted ha retirado {cantidad}$ de su cuenta. Su saldo actual es: {self.saldo}'
        elif self.saldo < cantidad:
            return f'Saldo insuficiente. Su saldo actual es: {self.saldo}$'
    
    def __str__(self) -> str:
        return f'Titular: {self.titular}\nSaldo Disponible: {self.saldo}'

def menu():
    print('''Seleccione las siguientes opciones para interartuar con su cuenta: 
    1. Información de la cuenta
    2. Depositar dinero
    3. Retirar dinero
    q. Salir''')

person = Cuenta('Fer')

while True:
    print('==================================')
    menu()
    option = input('Indique una opcion: ')
    if option == '1':
        print('\n==================================')
        print(person)
        print('==================================\n')
    elif option == '2':
        print('\n==================================')
        try:
            print(person.deposito(int(input('Ingrese la cantidad del deposito: '))))
        except ValueError:
            print('Error. El valor introducido es invalido')
        print('==================================\n')
    elif option == '3':
        print('\n==================================')
        try:
            print(person.retiro(int(input('Ingrese la cantidad del retiro: '))))
        except ValueError:
            print('Error. El valor introducido es invalido')
        print('==================================\n')
    elif option.lower() == 'q':
        print('Gracias por usar nuestro sistema bancario. Hasta luego')
        break
    else:
        print('Opcion Invalida. Intente de nuevo')