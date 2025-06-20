""" 
Tienes poder sobre tu mente, no sobre los 
acontecimientos. Date cuenta de esto y 
encontrarás la fuerza.
"""


#Lista enlazada simple

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
    
    # Inserción al principio de la lista enlazada
    def insertar_al_principio(self, elemento):
        nuevo_nodo = Nodo(elemento) 
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
    
    # Inserción al final de la lista enlazada
    def insertar_al_final(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.head is not None:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = nuevo_nodo
        else:
            self.head = nuevo_nodo
    
    def insertar_en_posicion(self, position: int, elemento):
        nuevo_nodo = Nodo(elemento)
        if position == 1:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        else:
            current = self.head
            cont = 0
            while current is not None and cont < position-1:
                cont += 1
                current = current.next
            nuevo_nodo.next = current.next
            current.next = nuevo_nodo
    
    def print_list(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
        else:
            print('No hay datos para mostrar. Lista vacia')

lista = ListaEnlazadaSimple()

lista.insertar_al_final(83)
lista.insertar_al_final(93)
lista.insertar_al_principio(35)
lista.insertar_al_final(70)
lista.insertar_en_posicion(1, 68)
lista.insertar_en_posicion(3, 25)

lista.print_list()
