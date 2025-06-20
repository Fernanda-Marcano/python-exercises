class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def insert_last(self, element):
        new_node = Node(element)
        if self.head is not None:
            current = self.head 
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def insert_position(self, position:int, element):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            cont = 1
            while current.next is not None and cont < position-1:
                current = current.next
                cont += 1
            if position == 1:
                self.head = new_node
            else:
                new_node.next = current.next
                current.next = new_node
    
    def delete_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            del temp
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            previous = None
            while temp.next is not None:
                previous = temp
                temp = temp.next
            previous.next = temp.next
            del temp
    
    def delete_position(self, position:int):
        if self.head is not None:
            temp = self.head
            previous = None
            cont = 1
            while temp.next is not None and cont < position:
                previous = temp
                temp = temp.next
                cont += 1
            if position == 1:
                self.head = temp.next
                del temp
            else:
                previous.next = temp.next
                del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('No existen elementos almacenados en la lista')


lista = SimpleLinkedList()
lista.insert_first(20)
lista.insert_first(30)
lista.print_list()
print()
lista.insert_last(45)
lista.insert_last(70)
lista.print_list()
print()
lista.insert_position(2, 700)
lista.print_list()