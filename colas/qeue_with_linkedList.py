#Escribir la estructura de una cola usando una lista enlazada simple
#Las colas siguen la instruccion FIFO (El primero en entrar es el primero en salir)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, element:int):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def delete_last(self):
        if self.head is not None:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            del temp
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next