'''
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
'''

class Node:
    def __init__(self, key): 
        self.key = key  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.key) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    
    height = 0
    if root.left is not None:
        height = 1 + height(root.left)
    if root.right is not None:
        height = 1 + height(root.right)
    
    return height

tree = BinarySearchTree()

tree.create(1)
tree.create(2)
tree.create(3)
tree.create(4)
tree.create(5)

print(height(tree))
