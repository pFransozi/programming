'''
Linked list addresses some of the limitations of arrays, which are: array is a static structure, 
and cannot easily extended or reduced to fit the data set.

Rather, a linked list is a linear dynamic data structure. The number of nodes is not fixed and
can grow and shrink on demand.

Node: data and ref. next node.
Last node has a ref. next node == None

The entry point node is called head, and the last one is called tail.
The head is the ref. to the first node, and if it is None, the list is empty.

Summary:

1. Successive elements are connected by pointers
2. The last element points to None
3. Can grow or shrink in size during execution of a program
4. Can be made just as long as required (actually, until system memory exhausts)
5. Does not waste memory space (but takes some extra memory for pointers). It allocates
memory as list grows.

Operations:

insert: insert element into the list
delete: removes and return the specified position element from the list
delete list: remove all elements in the list
count: return the number of elements in the list
find nth: find nth node from the end of the list

Difference (when one is suitable or not) between Arrays and Linked Lists

Array:
    1. one memory block is allocated for the array. For that, the access to the elements is in
    a constant time, using the index if the particular element.
        1. consider the address of the first position of the array
        2. calculate the size of of one element;
        3. multiply the size by the index;
        4. with this result count from the address of the first position
        5. this process takes two constant operation (*, +), which are constant operations. 
        Therefore, access an element in an array has time complexity constant, in any complexity
        is 1.
    2. Advantages: simple and easy to use; Faster access to the elements (constant access)
    3. Disadvantages: 
        1.preallocates all needed memory, and wastes memory space for indices in the array
        that are empty
        2. fixed size: the size of the array is static
        3. work with one block allocation: a big array declared in compile time, may be not
        possible to get memory in runtime
        4. complex position-based insertion: to insert an element at a given position, werandint
        create the new array double the size ot the original array.
        b. similarly, reduce the array size to half if the elements in the array are less than
        half.

Linked list:
    1.advantages:
        a) can be expanded in a constant time; adding a new element on the list is easily
        without the need to do any copying and reallocating (using a array, the adding requires 
        reallocation, shifting the elements to open space for the new one; and when the array 
        is full, a resize is required)
    2. disadvantages:
        a) access time to individual elements. Array is random access, which means O(1).
        Linked List is O(n) to access an element in the worst case.
        b) spacial locality in memory. Arrays are defined as contiguous blocks of memory,
        and so any array element will be physically near. 
    3. Linked list can be hard to manipulate. If the last element is deleted, O(n), 
    the last element but one will be changed, changing the ref. next node to None. In this
    process the list must be traversed O(n).

Comparison

Parameter               |   Linked List     | Array     |   Dynamic Array
Indexing                     O(n)               O(1)         O(1)
Ins/Del at beginning         O(1)               O(n)(a)      O(n)
Ins at end                   O(n)               O(1)(b)      O(1) [if array is not full]
                                                             O(n) [if the array is full. the resizing]
Del at ending                O(n)               O(1)         O(n)
Ins in middle                O(n)               O(n)(a)      O(n)
Del in middle                O(n)               O(n)(a)      O(n)
Wasted space                 O(n)[for pointers] 0            O(n)



(a): if array is not full (for shifting elements)
(b): if array is not full
'''

from unittest import TestCase
import random

#the base element in a linked list
class Node():

    def __init__(self, data=None, next=None):
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

    #return true if self has a next node.
    def has_next(self):
        return self.next != None
    
    def __str__(self) -> str:
        return f'Data: {self.data}, Next: {self.next}'

# class that define Linked List
class LinkedList(object):
    '''
    basic operations:
    traversing the list
    ins an item in the list
    del an item from the list
    '''

    def __init__(self, node:Node=None):

        #in this case, there's a new node.
        if node != None:
            self.length = 1
        else:
            self.length = 0
        self.head = node

    def length_list(self) -> int:
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.next

        #update the length
        self.length = count
        return count

    #a recursive alternative to get list length seems not appropriate. Think about
    # the space complexity due to stacking calls. But, this is an exercise.
    def length_list_recur(self, next:Node) -> int:
        
        if next == None:
            return 1
        else:
            return 1 + self.length_list_recur(next.next)

    def traverse(self):

        #basic constraints
        if self.head == None: 
            print("None")
        else:
            current = self.head
            print(current.data, end='')
            
            while(current.next != None):
                current = current.next
                print(f' -> {current.data}', end='')
            else:
                print('\n')

    def get_node(self, data):

        if self.length == 0:
            raise ValueError("The list is empty.")
        else:

            current = self.head
            found = False

            while not found:

                if current == None:
                    raise ValueError(f"Data ({data}) not found.")
                elif current.data == data:
                    found = True
                else:
                    current = current.next
            
            if found: return current



    def insert_at_beginning(self, data):
        
        newNode = Node(data)

        if self.head != None:
            newNode.next = self.head
            self.head = newNode
        
        else: 
            self.head = newNode
        
        # update the length attribute.
        self.length +=  1

    def insert_at_end(self, data):

        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else: # in this case, the algorithm find the last node, which means the node has no next.

            current = self.head
            while current.next != None:
                current = current.next
            
            current.next = newNode
            self.length += 1 

    def insert_at(self, position:int, data):
        
        #basic constraints
        if position > self.length or position < 1: 
            print(f"Invalid position {position}, node does not added.")
            return None
        else:

            # two basic insertions: 
            #               position == 0 (at beginning), 
            #               position == self.length (at end)
            if position == 1:
                self.insert_at_beginning(data)
            elif position == self.length:
                self.insert_at_end(data)
            else: # any insertion between 0 and self.length

                newNode = Node(data)

                current = self.head
                count_node = 1

                #find pre-node position, which means node at (position -1)
                while count_node < position -1 and current.next != None:
                    current = current.next
                    count_node += 1 

                #change the link
                #the newNode will be at pre-node.next position, so newNode.next will be
                #linked with pre-node.next
                newNode.next = current.next
                #and the pre-node.next is linked with the newNode
                current.next = newNode

                #increment self.length
                self.length += 1

    #remove the first node, which is the self.head
    def delete_at_beginning(self):
        
        #basic constraints
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    #remove the last node.
    def delete_at_end(self):
        
        #basic constraints
        if self.length == 0:
            print("The list is empty")
        else:

            current = self.head
            prev_current = None

            while current.next != None:
                prev_current = current
                current = current.next

            if prev_current == None:
                self.head = current.next
            else:
                prev_current.next = None
                self.length -= 1

    def delete_at_position(self, position):

        #basic constraint
        if self.length == 0:
            print("The list is empty")
        else:
            
            #basic constraint, if an outbound position, no node deleted.
            if position < 1 or position > self.length:
                print(f"Position argument ({position}) invalid, no node deleted")
            else:

                #basic position: 1 - delete the first; position == self.length: delete the last
                if position == 1:
                    self.delete_at_beginning()
                elif position == self.length:
                    self.delete_at_end()
                else: #delete at position between 1 and self.length

                    current = self.head
                    prev_current = self
                    count_nodes = 1 

                    while count_nodes < position and current.next != None:
                        prev_current = current
                        current = current.next
                        count_nodes += 1

                    prev_current.next = current.next
                    self.length -= 1
    
    #delete the first node that was found based on node argument
    def delete_node(self, node:Node):

        # basic constraints
        if self.length == 0:
            raise ValueError("The list is empty")
        elif node == None:
            raise ValueError(f"Invalid node argument ({None})")
        else:

            current_node = self.head
            prev_node = None
            found = False

            while not found:

                # basic constraints
                if current_node == None:
                    raise ValueError(f"Node ({str(node)}) not founded in list.")
                elif current_node == node:
                    found = True
                else:
                    prev_node = current_node
                    current_node = current_node.next
                
            if prev_node == None:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next

            self.length -= 1
        
    def delete_value(self, value):

        # basic constraint
        if self.length == 0:
            raise ValueError("The list is empty.")
        else:

            current_node = self.head
            prev_node = None
            found = False

            while not found:

                
                if current_node == None: #reach None node related to the last valid Node.
                    raise ValueError(f"Value ({value}) not found.")
                elif current_node.data == value:
                    found = True
                else:
                    prev_node = current_node
                    current_node = current_node.next
            
            if prev_node == None:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next
            
            self.length -= 1

    # this get middle is based on turtle and hare algorithm.
    def get_middle(self, node):

        if node is None: return node

        fast = node
        slow = node

        while fast.next is not None and \
                fast.next.next is not None:
            
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):

        head = Node(-1)
        sorted_tmp = head


        while left is not None and right is not None:

            if left.data <= right.data:
                sorted_tmp.next = left
                left = left.next
            else:
                sorted_tmp.next = right
                right = right.next
            
            sorted_tmp = sorted_tmp.next

        while left is not None:
            sorted_tmp.next = left

            #move forward
            left = left.next
            sorted_tmp = sorted_tmp.next

        while right is not None:
            sorted_tmp.next = right

            #move forward
            right = right.next
            sorted_tmp = sorted_tmp.next

        return head.next
        
    
    def merge_sort(self, head):

        # base case. this if will stop recursive call when reach one node.
        if head is None or head.next is None:
            return head

        middle_before = self.get_middle(head)
        middle_after = middle_before.next

        middle_before.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(middle_after)

        sorted_list = self._merge(left, right)

        return sorted_list

    def binary_search(self, data, head:Node) -> Node:

        middle_before = self.get_middle(head)







linkedListTestSort = LinkedList()

for _ in range(0, 200):
    linkedListTestSort.insert_at_end(random.randint(0, 10000000))

linkedListTestSort.traverse()
sorted_list = linkedListTestSort.merge_sort(linkedListTestSort.head)
linkedListTestSort.head = sorted_list
linkedListTestSort.traverse()



# linkedList = LinkedList()
# linkedList.insert_at_beginning(0)
# linkedList.insert_at_end(1)
# linkedList.insert_at_end(2)
# linkedList.insert_at_end(3)

# len_ll = linkedList.length_list()
# len_ll_rec = linkedList.length_list_recur(linkedList.head.next)

# TestCase().assertEqual(len_ll, 4, 'Get list length return wrong length')
# TestCase().assertEqual(len_ll_rec, 4, 'Get list length recursively return wrong length')
# TestCase().assertEqual(len_ll_rec, len_ll, 'Get len dynamically differ get len recursively')

# linkedList.traverse()

# linkedList.insert_at(1, 'a')
# linkedList.insert_at(3, 'b')
# linkedList.insert_at(6, 'c')
# linkedList.traverse()

# linkedList.delete_at_end()
# linkedList.delete_at_beginning()
# linkedList.delete_at_position(2)
# linkedList.traverse()

# linkedList.insert_at(2, 'a')
# linkedList.insert_at(2, 'b')
# linkedList.insert_at(2, 'c')
# linkedList.insert_at(5, 'c')
# linkedList.insert_at(5, 'b')
# linkedList.insert_at(5, 'a')
# linkedList.traverse()

# linkedList.delete_value('a')
# linkedList.delete_value('b')
# linkedList.delete_value('c')
# linkedList.traverse()

# linkedList.delete_node(linkedList.get_node('a'))
# linkedList.delete_node(linkedList.get_node('b'))
# linkedList.delete_node(linkedList.get_node('c'))
# linkedList.traverse()

# linkedList.delete_node(linkedList.get_node(3))
# linkedList.delete_node(linkedList.get_node(2))
# linkedList.traverse()

# linkedList.delete_at_beginning()
# linkedList.traverse()
# linkedList.delete_at_beginning()
# linkedList.traverse()

# linkedList.insert_at_beginning(0)
# linkedList.insert_at_beginning(1)
# linkedList.traverse()

# linkedList.delete_at_end()
# linkedList.delete_at_end()
# linkedList.traverse()



