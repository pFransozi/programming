'''

basic operations:

traverse_preorder: time complexity: O(n), space_complexity: O(n)
traverse_preorder_iterative: time complexity: O(n), space complexity: O(n)

traverse_inorder: time complexity: O(n), space complexity: O(n)
traverse_inorder_iterative: time complexity: O(n), space complexity: O(n)

'''

class Node:

    def __init__(self, data) -> None:
        
        self.__data = data
        self.__left = None
        self.__right = None
    
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_left(self, left):
        self.__left = left
    
    def get_left(self):
        return self.__left

    def set_right(self, right):
        self.__right = right
    
    def get_right(self):
        return self.__right


class BinaryTree:

    def __init__(self, root:Node=None) -> None:
        
        self.__root = root

    def get_root(self) -> None:
        return self.__root

    def set_root(self, root:Node):
        self.__root = root

    def get_height(self, root:Node) -> int:
        
        count_height = 0

        if root

    'Preorder means: process the current node, visit left, visit right'
    def traverse_preorder(self, root:Node):

        #base case, constraints
        if root is None:
            return

        print(f"{root.get_data()}", end='-->', sep='-->')

        self.traverse_preorder(root.get_left())
        self.traverse_preorder(root.get_right())

    def traverse_preorder_iterative(self, root:Node, result:list):
        
        # case base, constraints
        if root is None:
            return

        stack = [] # store the next node, which will be processed.
        stack.append(root)

        while stack:

            node = stack.pop() # node that need to be processed
            result.append(node) #processed

            #visit the next nodes
            right = node.get_right()
            left = node.get_left()
            
            # store to process in the next iteration
            if right: stack.append()
            if left: stack.append()

    'Inorder means: go forward to the last node at left branch, process it, then process right'
    def traverse_inorder(self, root:Node):

        #case base, constraints
        if root is None:
            return

        self.traverse_inorder(root.get_left())
        print(f"{root.get_data()}", end='-->', sep='-->')
        self.traverse_inorder(root.get_right())

    def traverse_inorder_iterative(self, root, result:list):

        #base case, constraints
        if root is None:
            return

        stack = []
        node = root

        '''
        the basic idea is: go forward through left branch until a null node.
        When reach this node, pop the last left, process, and set the right to process
        in the next loop.
        
        '''
        while stack or node:

            if node:
                stack.append(node)
                node = node.get_left()
            else:
                node = stack.pop()
                result.append(node)
                node = node.get_right()
        

    

        


    
