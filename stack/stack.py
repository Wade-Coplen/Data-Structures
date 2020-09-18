"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value, next_node= None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next
    

class LinkedList:
    def __init__(self):
            # what attributes do we need?
            #set initial state of node
            self.head = None
            self.tail = None
    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)
        if self.head is None:
            return None
        else:
            # set next_node of my newNode to the head
            new_node.set_next_node(self.head)
            # update head attribute            
            self.head = new_node
        
    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # if LL is empty
        if self.head == None:
            return None
            #update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. If LL is not empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            #update self.tail
            self.tail = new_node

    def remove_head(self):
        # if LL is empty
        if self.head is None:
            return None
        else:
            # return the value of the old head
            return_value = self.head.get.value()
            #list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            #lists with >2 elements
            else:
                self.head = self.head.get_next_node()
                return return_value
    def remove_tail(self):
        # TODO
        # if the there is an empty list?
        if self.tail == None:
            return None
        else:
            #value of previous head
            # return_value = self.head.get.value()
        # list with 1 element?
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
            # list with >2 elements?
                self.head = self.head.get_next_node()
                return return_value
                
        
    def contains(self, value):
        # TODO time permitting
        current_node = self.head
        while current_node == None:
            # if we find 'value'
            if current_node.get_value() == value:
                return True
            return False
    def get_max(self):
        # TODO time permitting
        pass




"""
class Empty(Exception):
    pass
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0

    def __len__(self):
        return len(self.storage)  
        
    def push(self, value):
        """
        Push the elements at the Last index
        :return: None
        """
        self.storage.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.storage.pop()
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print('Stack', s.storage)
print('Length', len(s))
print('Is empty', s.is_empty())
print('Popped', s.pop())
print('Stack', s.storage)
"""

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass