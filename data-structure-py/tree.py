'''
Ideally, trees should have a height of floor(log2(n)), where n is the number of nodes 
in the tree. Is it possible for a tree to be "balanced" under the definition in this section, 
but be taller than floor(log2(n))?
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):

        if self.data == target:
            return self

        if self.left and target < self.data:
            return self.left.search(target)
        
        if self.right and target > self.data:
            return self.right.search(target)

        return None

    def add(self, data):

        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else: 
                self.left.add(data)
                self.left = self.left.fixImbalanceIfExists()
        
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else: 
                self.right.add(data)
                self.right = self.right.fixImbalanceIfExists()

        return None

    def findMin(self):
        if self.left:
            return self.left.findMin()
        
        return self.data


    def delete(self, target):
        
        if self.data == target:
            
            if self.left and self.right: # so RTFM = right tree find minimum.
                
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)
                return self
            else:
                return self.left or self.right

        if self.right and target > self.data:
            self.right = self.right.delete(target)
        if self.left and target < self.data:
            self.left = self.left.delete(target)

        return self.fixImbalanceIfExists()

    def toStr(self) :

        if not self.isBalanced():
            return f'{self.data}*'
        return f'{self.data}'

    def traversePreorder(self):
        
        print(self.data, end=",")

        if self.left: self.left.traversePreorder()
        if self.right: self.right.traversePreorder()

    
    def traverseInorder(self):

        if self.left: self.left.traverseInorder()

        print(self.data, end=",")

        if self.right: self.right.traverseInorder()

    def traversePostorder(self):

        if self.left: self.left.traversePostorder()
        if self.right: self.right.traversePostorder()

        print(self.data, end=",")

    def height(self, h=0):

        left_height = self.left.height(h + 1) if self.left else h
        right_height = self.right.height(h + 1) if self.right else h

        return max(left_height, right_height)

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self)
            return nodes

        if self.left: self.left.getNodesAtDepth(depth - 1, nodes)
        else: nodes.extend([None]*2**(depth-1))
        if self.right: self.right.getNodesAtDepth(depth - 1, nodes)
        else: nodes.extend([None]*2**(depth-1))

        return nodes
    
    def isBalanced(self):
        leftHeight = self.left.height() if self.left else 0
        rightHeight = self.right.height() if self.right else 0

        return abs(leftHeight - rightHeight) < 2

    def getLeftRightHeightDifference(self):
        leftHeight = self.left.height() if self.left else 0
        rightHeight = self.right.height() if self.right else 0

        return leftHeight - rightHeight

    def fixImbalanceIfExists(self):
        
        if self.getLeftRightHeightDifference() > 1: #left imbalance
            
            if self.getLeftRightHeightDifference() > 0: #left left imbalance
                return rotateRight(self) 
            else: #left right
                self.left = rotateLeft(self.left)
                return rotateRight(self)
        elif self.getLeftRightHeightDifference() < -1: #right imbalance
            
            if self.getLeftRightHeightDifference() < 0: #right right
                return rotateLeft(self)  
            else: #right left
                self.right = rotateRight(self.right)
                return rotateLeft(self)
        
        return self

    def rebalance(self):

        if self.left:
            self.left.rebalance()
            self.left = self.left.fixImbalanceIfExists()
        
        if self.right:
            self.right.rebalance()
            self.right = self.right.fixImbalanceIfExists()



'''

'''
class Tree:

    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def height(self):
        return self.root.height()

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def _nodeToChar(self, node, spacing):
        if node is None: return '_' + (' '*spacing)

        nodeStr = node.toStr()

        spacing = spacing - len(nodeStr) + 1
        return nodeStr + (' ' * spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(node, spacing) for node in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def add(self, data):
        self.root.add(data)
        self.root = self.root.fixImbalanceIfExists()

    def delete(self, target):
        self.root = self.root.delete(target)

    def rebalance(self):
        
        self.root.rebalance()
        self.root = self.root.fixImbalanceIfExists()


def rotateRight(root):
    
    pivot = root.left
    reattachNode = pivot.right
    root.left = reattachNode
    pivot.right = root

    return pivot

def rotateLeft(root):
    pivot = root.right
    reattachNote = pivot.left
    root.right = reattachNote
    pivot.left = root

    return pivot




#node = Node(50)

#node.left = Node(40)
#node.left.left = Node(30)
#node.left.left.left = Node(20)
#node.left.left.left.left = Node(10)
#node.left.left.left.left.left = Node(5)
#node.left.left.left.left.left.left = Node(1)
#node.left.left.right = Node(35)

#node.left.right = Node(45)


#node.right = Node(60)
#node.right.left = Node(55)
#node.right.right = Node(80)


# myTree = Tree(node, 'My Tree')
# print(myTree.root)
# search_result = myTree. search(40)
# print(search_result)

# print("\n===============================")
# myTree.traverseInorder()
# print("\n===============================")
# myTree.traversePreorder()
# print("\n===============================")
# myTree.traversePostorder()
# print("\n===============================")

# print(myTree.height())
# print(myTree.getNodesAtDepth(4))

# myTree.add(1)
# myTree.add(2)
# myTree.add(3)
# myTree.add(55)

# myTree.print()

# unbalancedLeftLeft = Tree(Node(30), 'UNBALANCED LEFT LEFT')
# unbalancedLeftLeft.root.left = Node(20)
# unbalancedLeftLeft.root.left.right = Node(21)
# unbalancedLeftLeft.root.left.left = Node(10)
# unbalancedLeftLeft.root.left.left.left = Node(9)
# unbalancedLeftLeft.root.left.left.right = Node(11)
# unbalancedLeftLeft.print()
# unbalancedLeftLeft.root = rotateRight(unbalancedLeftLeft.root)
# unbalancedLeftLeft.print()


# unbalancedRightRight = Tree(Node(10), 'UNBALANCED RIGHT RIGHT')
# unbalancedRightRight.root.right = Node(20)
# unbalancedRightRight.root.right.left = Node(19)
# unbalancedRightRight.root.right.right = Node(30)
# unbalancedRightRight.root.right.right.left = Node(29)
# unbalancedRightRight.root.right.right.right = Node(31)
# unbalancedRightRight.print()
# unbalancedRightRight.root = rotateLeft(unbalancedRightRight.root)
# unbalancedRightRight.print()



# unbalancedLeftRight = Tree(Node(30), 'UNBALANCED LEFT RIGHT')
# unbalancedLeftRight.root.right = Node(31)
# unbalancedLeftRight.root.left = Node(10)
# unbalancedLeftRight.root.left.right = Node(20)
# unbalancedLeftRight.root.left.left = Node(9)
# unbalancedLeftRight.root.left.right.left = Node(19)
# unbalancedLeftRight.root.left.right.right = Node(21)
# unbalancedLeftRight.print()

# unbalancedLeftRight.root.left = rotateLeft(unbalancedLeftRight.root.left)
# unbalancedLeftRight.root = rotateRight(unbalancedLeftRight.root)
# unbalancedLeftRight.print()


# unbalancedRightLeft = Tree(Node(30), 'UNBALANCED RIGHT LEFT')
# unbalancedRightLeft.root.left = Node(31)
# unbalancedRightLeft.root.right = Node(10)
# unbalancedRightLeft.root.right.left = Node(20)
# unbalancedRightLeft.root.right.right = Node(9)
# unbalancedRightLeft.root.right.left.right = Node(19)
# unbalancedRightLeft.root.right.left.left = Node(21)
# unbalancedRightLeft.print()

# unbalancedRightLeft.root.right = rotateRight(unbalancedRightLeft.root.right)
# unbalancedRightLeft.root = rotateLeft(unbalancedRightLeft.root)
# unbalancedRightLeft.print()



tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)
tree.root.left.left.left.left.left = Node(1)
tree.print()

tree.rebalance()
tree.print()

height = tree.height()


#tree = Tree(Node(50))
#tree.add(25)
# tree.add(75)
# tree.add(10)
# tree.add(35)
# tree.add(30)
# tree.add(5)
# tree.add(2)
# tree.add(1)
# tree.print()

# tree.delete(50)
# tree.delete(75)
# tree.print()