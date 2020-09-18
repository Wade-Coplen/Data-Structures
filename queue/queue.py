"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
"""

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
        self.front = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        self.storage.append(value)
        self.size = self.size + 1
   

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.storage[self.front]
        self.storage[self.front] = None
        self.front = self.front +1
        self.size = self.size -1
        return value
    def first(self):
        if self.is_empty():
            return None
        return self.storage[self.front]

q = Queue()
q.enqueue(5)
q.enqueue(10)
print('Q', q.storage)
print('L', len(q))
print('DQ', q.dequeue())
print('Q', q.storage)
q.enqueue(15)
q.enqueue(20)
print('Q', q.storage)
print('First El', q.first())
print('DQ', q.dequeue())
print('Q', q.storage)

"""
class Node:
    __slots__ = 'element', 'next'
    def __init__(self, value, element, next_node= None):
        self.value = value
        self.next_node = next_node
        self.element = element
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
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new_node = Node(element, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.nex t = new_node
        self.tail = new_node
        self.size = self.size + 1


    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.elements
        self.head = self.head.next_node
        self.size = self.size -1
        if self.is_empty():
            self.tail = None
        return value
    def display(self):
        temp = self.head
        while temp:
            temp = temp.next_node
            print()

q = Queue()
q.enqueue(400)
q.enqueue(401)
q.display()
print('L', len(q))
print('DQ', q.dequeue())
q.display()
q.enqueue(402)
q.enqueue(403)
q.display()

