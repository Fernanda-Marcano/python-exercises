class Node:
    def __init__(self, data:int):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_last(self, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        else:
            self.head = new_node
    
    def insert_after_position(self, position:int, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            cont = 1
            while current.next is not None and cont < position:
                current = current.next
                cont += 1
            new_node.next = current.next
            new_node.prev = current
            if new_node.next is not None:
                new_node.next.prev = new_node
            current.next = new_node
    
    def insert_before_position(self, position:int, element:int):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            count = 1
            while current.next is not None and count < position:
                current = current.next
                count += 1
            new_node.prev = current.prev
            new_node.next = current
            if position == 1:
                self.head = new_node
            elif new_node.prev is not None:
                new_node.prev.next = new_node
            current.prev = new_node
    
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
            count = 1
            while temp.next is not None and count < position:
                temp = temp.next
                count += 1
            if position == 1:
                self.head = temp.next
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            del temp
    
    def search_node(self, data:int):
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.data == data:
                    return True
                current = current.next
            else:
                return False
    
    def length_list(self):
        if self.head is not None:
            current = self.head
            count = 0
            while current is not None:
                count += 1
                current = current.next
            return count
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
    
    def print_reversed_list(self):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            while current is not None:
                print(current.data, end=' ')
                current = current.prev

lista = DoublyLinkedList()

for element in range(10, 60, 10):
    lista.insert_last(element)
lista.delete_position(3)
lista.print_list()

print(lista.length_list())
