""" 
	Lista enlazada básica: 
	- Implementar una clase que represente una lista enlazada con operaciones básicas 
 	  como añadir y eliminar nodos. """

class Nodo:
    def __init__(self, dato):
        self.data = dato
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None: 
            self.head = nuevo_nodo
        else:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
    
    def insert_last(self, data):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            nuevo_nodo = Nodo(data)
            current.next = nuevo_nodo
        else:
            nuevo_nodo = Nodo(data)
            self.head = nuevo_nodo
    
    def delete_last(self):
        if self.head is None:
            print('No hay elementos que eliminar. Lista vacia')
        else:
            temp = self.head
            previous = None
            while temp.next is not None:
                previous = temp
                temp = temp.next
            previous.next = None
            del temp
            
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('No hay datos para mostrar. Lista vacia')

lista = SimpleLinkedList()

for i in range(10):
    lista.insert_first(i)

lista.print_list()