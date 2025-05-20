class Pila:
    def __init__(self):
        self.__items = []
    
    def push(self, data):
        self.__items.append(data)
    
    def empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def print_stack(self):
        return f'Primero ---> {self.__items}'
    
    def pop(self):
        if self.__items is not self.empty():
            return self.__items.pop()


class Cola:
    def __init__(self):
        self.__items = []
    
    def encolar(self, valor):
        self.__items.insert(0, valor)
    
    def desencolar(self):
        return self.__items.pop()
    
    def empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def mostrar(self):
        if self.__items is not self.empty():
            return self.__items
        else:
            return None

cola = Pila()

print(cola.print_stack())