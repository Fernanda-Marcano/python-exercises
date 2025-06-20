#Creando el funcionamiento de una pila usando una lista enlazada simple

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    #Cada elemento debe insertase al principio de la lista
    def insert_first(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    #Cada elemento debe eliminarse al principio de la lista
    def delete_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head 
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('Lista vacia')

lista = LinkedList()

for data in range(10, 60, 10):
    lista.insert_first(data)

lista.print_list()
lista.delete_first()
print()
lista.print_list()
print()
lista.delete_first()
lista.print_list()
print()
lista.delete_first()
lista.print_list()