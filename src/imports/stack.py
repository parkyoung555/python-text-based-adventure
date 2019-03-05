"""
Program Name: Stacks
Progammer: Young Park
Date: February 22, 2012
"""

class Stack():
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
       item = self.items.pop()
       return item
       
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)
    
    def top(self):
        if self.isEmpty():
            item = None
        else:
            item = self.items[-1]
        return item

    def size(self):
        return len(self.items)

    
