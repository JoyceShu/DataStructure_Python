from hashlib import new
from re import M


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        tmp = self.root
        while (True):
            if new_node.value == tmp.value:
                return False
            if new_node.value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)









 