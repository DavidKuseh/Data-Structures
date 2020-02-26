import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
    # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if self.left:
                # place our new node here
                self.left.insert(value)
            # otherwise
                # repeat process for the left
            else:
                self.left = BinarySearchTree(value)
     # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        elif value >= self.value:
            # does it have a child to the right?
            if self.right:
                # place our new node here
                self.right.insert(value)  
            # otherwise
                # repeat the process for the right 
            else:
                self.right = BinarySearchTree(value)   

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # BASE CASE
        if self.value == target:
            return True

        # LEFT CASE
        elif self.value > target:
            if self.left == None:
                return False
            return self.left.contains(target) 
        
        # RIGHT CASE
        else:
            if self.right == None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree
            # return none  
        if self.value == None:
            return None

        # recursive case
        # if there is no right value 
            # return the root node value
        if self.right == None:
            return self.value 
        
        # otherwise
            # return get max of the right hand child
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # base case
        if self.right is None and self.left is None:
            return None
        
        # left case
        else:
            if self.left:
                self.left.for_each(cb)
                
        # right case
            if self.right:
                self.right.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
