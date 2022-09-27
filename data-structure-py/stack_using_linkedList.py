'''
Implementation of a stack using a linked List.

Main operations are:

-> push: insert an element in the stack
-> pop: remove an element from the stack
-> peek: get the value of the without remove

Stack if LIFO

'''

from inspect import stack


class Node:

    def __init__(self, data, next=None):
        
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None


class Stack:

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, item:Node):

        if self.top is None:
            self.top = item
        else:
            tmp_item = self.top
            self.top = item
            self.top.set_next(tmp_item)

        self.length += 1

    def pop(self) -> Node:
        
        #basic constraints
        if self.length == 0:
            raise ValueError("The stack is empty")
        else:
            pop_item = self.top
            self.top = pop_item.get_next()
            self.length -= 1
            return pop_item

    def peek(self):

        #basic constraints
        if self.length == 0:
            raise ValueError("The stack is empty")       
        else:
            return self.top.get_data()

    def size(self):
        return self.length


# stack = Stack()
# stack.push(Node('p'))
# stack.push(Node('h'))
# stack.push(Node('i'))
# stack.push(Node('l'))
# stack.push(Node('i'))
# stack.push(Node('p'))
# stack.push(Node('e'))
        
# while stack.size() > 0:
#     print(stack.pop().get_data(), end='')

# print('\n')

mapping_symbols = {')':'(', '}':'{', ']':'['}
expression = '(2+3)*(5/(2*4))([])'
check_balance_symbols = Stack()
unbalanced = False

for char in expression:

    if char in mapping_symbols: # look for the key, which is an close symbol
        top_symbol = check_balance_symbols.pop().data if check_balance_symbols.size() > 0 else '#'

        if mapping_symbols[char] != top_symbol:
            unbalanced = True
            break
    
    else:
        if char not in mapping_symbols.values():
            continue
        else: check_balance_symbols.push(Node(char))

unbalanced = (check_balance_symbols.size() > 0) if not unbalanced else unbalanced


print("Expression unbalanced" if unbalanced else "Expression balanced")