
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
    def __init__(self, node= None):
            # what attributes do we need?
            #set initial state of node
            self.head = node
            self.tail = node
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

