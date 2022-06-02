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
    def contain(self, value):
        if self.root is None:
            return False
        tmp = self.root
        
        while tmp is not None:
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            else:
                return True
        return False
    
    def min_Value_node(self, cur_node):
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)

print(my_tree.min_Value_node(my_tree.root))
print(my_tree.min_Value_node(my_tree.root.right))
