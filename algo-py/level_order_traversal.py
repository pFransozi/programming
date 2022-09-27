'''
deque: 



'''
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

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


from collections import deque

def levelOrder(root):

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.info, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


tree = BinarySearchTree()
t = [1, 2, 3, 4, 5, 6]
for i in range(len(t)):
    tree.create(t[i])