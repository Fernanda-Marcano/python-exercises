class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, element):
        new_node = Node(element)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def delete_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            del temp
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            if temp.next is None:
                temp.prev.next = None
            del temp
    
    def delete_position(self, position:int):
        if self.head is not None:
            temp = self.head
            cont = 1
            while temp.next is not None and cont < position:
                temp =  temp.next
                cont += 1
            if position == 1:
                self.head = temp.next
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next


lista = DoublyLinkedList()

for element in range(20, 31):
    lista.insert_first(element)
lista.print_list()

lista.delete_first()
print()
lista.print_list()

lista.delete_last()
lista.delete_last()
print()
lista.print_list()

lista.delete_position(1)
print()
print('Eliminar en posicion 1:')
lista.print_list()

lista.delete_position(3)
print()
print('Eliminar en posicion 3:')
lista.print_list()

lista.delete_position(1)
print()
lista.print_list()