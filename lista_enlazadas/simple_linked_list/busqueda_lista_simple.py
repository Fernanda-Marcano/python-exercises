class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_to_first(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def search_node(self, element):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                if current.data == element:
                    return True
                current = current.next
            else:
                return False
    
    def length_list(self):
        current = self.head
        cont = 0
        while current.next is not None:
            cont += 1
            current = current.next
        return cont
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('No existen registros')

lista = LinkedList()

for i in range(20, 31):
    lista.insert_to_first(i)

lista.print_list()
print()
print(lista.search_node(28))
print()
print(lista.length_list())