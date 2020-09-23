

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev        
        self.next = next
        self.value = value
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node
        # adding to an empty 
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # or not empty list
        else:
            new_node.next = self.head #assign 
            #self.head.prev = new_node.next
            self.head.prev = new_node
            self.head = new_node
        # update length
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #save value to return
        # delete head
        #update self.head
        # return value
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            value = self.head.value
            self.delete(self.head)
            return value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        #if empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #if 1 or more nodes
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        # delete node
        self.delete(node)
        self.add_to_head(node.value)
        
    
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        '''
        # dont need to return value
        # need to update head and tail
        '''
        if self.head is None:
            return None
        elif self.head == self.tail:    
            self.head = None
            self.tail = None
        elif node is self.head: # 2 or more items
            self.head = node.next
            node.delete() # updating previou and or next pointers
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else: 
            node.delete()
        self.length -= 1
        
    
    ##Finds and returns the maximum value of all the nodes 
    #in the List.
    
    def get_max(self):
        # check if list is empty
        if self.head is None:
            return None
        # keep track at current node
        # keep track of current sum
        cur_node = self.head
        max_value = self.head.value
        # loop through all
        while cur_node:
            #comparing with cur_max
            
            if cur_node.value > max_value:
                max_value = cur_node.value
            cur_node = cur_node.next
        # return max
        return max_value
    