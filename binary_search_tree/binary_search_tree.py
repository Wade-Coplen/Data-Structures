"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None
        self.size = 0      
    def Print(self):
        print(self.value)
    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left= BSTNode(value)
                else: 
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        '''def Print(self):
            if self.left:
                self.left.Print()
            print( self.value),
            if self.right:
                self.right.Print()'''       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        
        while self.root:
            if target < self.root.value:
                self.root = self.root.left
            elif target > self.root.value:
                self.root = self.root.right
            else:
                return True
        return False
        
        # check to see if self.value is target
        # if yes return true
        # if no, go left or right?

    # Return the maximum value found in the tree
    def get_maxValue(self):
        if self.root:
            return self.get_maxValue(self.root)
        # go right until you cannot go anymore
        # return the value at the far right
    def get_max(self):
        if self.right:
            return self.get_max(self.right)

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        # go left, call fn() for each node
        # go right, call fn() for each node

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    # what is our stopping point?
    def in_order_print(self):
        
        while self.root:
            if self.left is None:
                return self.root
            if self.value < self.root:
                return self.left.value
            if self.value > self.root:
                return self.right.value
        print(value)

        #using in_order, print nodes in non decreasing order
        #4,2,5,1,3
        #inorder(node):
        #   if node == null then return
        #   inorder(node.left)
        #   visit(node)
        #   inorder(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
         
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
      pass
        

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
#bst.in_order_dft()
print("post order")
bst.post_order_dft()  
