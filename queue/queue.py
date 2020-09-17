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

