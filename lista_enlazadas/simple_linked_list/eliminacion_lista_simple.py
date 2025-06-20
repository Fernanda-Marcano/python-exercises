# Eliminar nodos de una lista enlazada simple

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
    
    def insertar_al_final(self, elemento):
        nuevo_nodo = Node(elemento)
        if self.head is not None:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = nuevo_nodo
        else:
            self.head = nuevo_nodo
    
    def eliminar_al_principio(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            del temp
        else:
            print('Lista Vacia')
    
    def eliminar_al_final(self):
        if self.head is not None:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = current.next
            del current
        else:
            print('Lista vacia')
    
    def eliminar_en_posicion(self, position:int):
        if self.head is not None:
            current = self.head
            previous = None
            cont = 1
            while current.next is not None and cont < position:
                previous = current
                current = current.next
                cont += 1
            if current == self.head:
                self.head = current.next
                del current
            else:
                previous.next = current.next
                del current
        else:
            print('Lista vacia')
    
    def actualizar_valor(self, position:int, dato):
        if self.head is None and position > 1:
            print('Lista vacia')
            return
        elif self.head is None and position == 1:
            nuevo_nodo = Node(dato)
            self.head = nuevo_nodo
        else:
            current = self.head
            cont = 1
            while current.next is not None and cont < position:
                current = current.next
                cont += 1
            if position == cont:
                current.data = dato
            else:
                print('No existen suficientes elementos en la lista, para actualizar ese valor')
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('No existen datos')


l = ListaEnlazadaSimple()
l.insertar_al_final(30)
l.insertar_al_final(38)
l.insertar_al_final(20)
l.print_list()