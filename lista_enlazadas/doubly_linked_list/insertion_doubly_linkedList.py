class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertion_first(self, element):
        new_node = Node(element)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insertion_last(self, element):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def insertion_after_node(self, element, position:int):
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
    
    def insertion_before_node(self, element, position):
        new_node = Node(element)
        if self.head is not None:
            current = self.head
            cont = 1
            while current.next is not None and cont < position:
                current = current.next
                cont += 1
            new_node.prev = current.prev
            new_node.next = current
            if new_node.prev is not None:
                new_node.prev.next = new_node
            current.prev = new_node
            if position == 1:
                self.head = new_node
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next

lista = DoublyLinkedList()
lista.insertion_first(45)
lista.insertion_first(50)
lista.insertion_first(100)
lista.print_list()
print()
lista.insertion_after_node(500, 2)
lista.insertion_after_node(60, 4)
lista.print_list()
print()
lista.insertion_before_node(400, 1)
lista.insertion_before_node(33, 2)
lista.print_list()