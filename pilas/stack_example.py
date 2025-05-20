class Pila:
    def __init__(self):
        self.items = [1,2,3,4]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items is not self.is_empty():
            print(self.items.pop())
        else:
            return None
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.items is not self.is_empty():
            return self.items[-1]
        else:
            return None


pila = Pila()
print(pila.peek())