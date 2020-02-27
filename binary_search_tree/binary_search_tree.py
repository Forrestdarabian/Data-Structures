from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if our nodes value is less than the current nodes value
        if value < self.value:
            # if it has a child to the left, place our new node there
            if self.left:
                self.left.insert(value)
            # if it doesnt, repeat the process
            else:
                self.left = BinarySearchTree(value)
        # same idea for right side except were checking if
        #  the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

# DFT Steps:
# initialize a stack
# push root to stack
# while stack not empty
# pop top item out of stack into temp
# DO THE THING!!!!!!
# if temp has right right put into stack
# if temp has left left put into stack

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        if node.right:
            print(node.value)
            self.in_order_print(node.right)
        else:
            print(node.value)


#     BFT Steps:
# initialize a queue
# push root to queue
# while stack not empty
# pop top item out of queue into temp
# DO THE THING!!!!!!
# if temp has right right put into queue
# if temp has left left put into queue

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current_node = queue.dequeue().value
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

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
