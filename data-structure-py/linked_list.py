'''

This code implements a linked list node with two attributes, which are value and next node. And it implements a wrapping of linked list with the main methods.

1. Traverse method traverse the list from the head none until a null next node. The time complexity is O(n);

2. Append method adds a new node at the end of the list. Therefore, the methods traverse the list until the last node. For that, the time complexity is O(n);

3. Peek method get the node in the position pass by argument to the function. In the worst case, which means the last node, the complexity is O(n);

4. Insert method adds a new node in a specific position. In the worst case the complexity is O(n).

5. Delete method deletes a node based on the value pass by argument to the method. In the worst case, which means the last node, the complexity is O(n);

6. Get middle method gets the middle of the list using Tortoise and Hare algorithm. That algorithm uses two pointers, one running double than another. When the fast reaches the end, the slow is in the meddle.
Complexity time is O(n) and complexity space is O(1) because the algorithm does not use extra memory.

7. In the wrapped class, there are two merge sort methods. One uses a recursive approach, and another uses a dynamic approach.
    Considering the recursive approach, the time complexity is O(n*log n), as the same for the space complexity O(n*log n).
    Considering the dynamic, the time complexity is O(n*log n), but the space complexity is O(log n).

    The space complexity difference is based on the size of recursive stack.


'''


from unittest import TestCase
import random


class Node(object):

    def __init__(self, value):
        
        self.value = value
        self.next = None

class LinkedList(object):
    
    def __init__(self, head=None):
        
        self.head = head

    def traverse(self):

        current = self.head
        
        if current is None: print('None')
        else:
            while current is not None:

                if current.next is not None: print(f'{current.value} -> ', end='')
                else:                              print(f'{current.value}')
                current = current.next

    def append(self, node):

        current = self.head
        
        if self.head: 
            while current.next: current = current.next
            current.next = node
        
        else: self.head = node

    def peek(self, position) -> Node:
        
        count_pos = 1
        current = self.head
        
        if self.head:
            
            if count_pos == position: return current
            while current.next:
                count_pos += 1
                if count_pos == position: return current.next
                current = current.next
            
            return None
        else: return None

    def insert(self, node, position):
        
        # the algorithm needs the node before the position for link the new node.
        current = self.peek(position -1)
            
        if current is None:
            return None
        else:
            node.next = current.next
            current.next = node

    def delete(self, value):
        
        if self.head is None: return None
        if self.head.value == value:
            self.head = self.head.next
            return None
            
        current = self.head.next
        while current.next is not None:
            
            if current.next.value == value: break
            current = current.next
        
        if current is None: return None
        else: current.next = current.next.next

    # O(n)
    def len(self):

        if self.head is None: return 0
        
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def get_middle(self, head) -> Node:

        if head == None:
            return head

        slow = head
        fast = head

        while(fast.next != None and
                fast.next.next != None):

            slow = slow.next
            fast = fast.next.next

        return slow

    
    def merge_sort(self, head):
        if head == None or head.next == None:
            return head

        def merge(a, b):
        
            result = None

            #base cases
            if a == None: return b
            if b == None: return a

            if a.value <= b.value:
                result = a
                result.next = merge(a.next, b)
            else:
                result = b
                result.next = merge(a, b.next)

            return result 



        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sortedList = merge(left, right)

        return sortedList

    
    def merge_sort1(self, head):

        def merge(a, b):

            merged = Node(-1)
            temp = merged

            while a is not None and b is not None:

                if a.value <= b.value:
                    temp.next = a
                    a = a.next
                else:
                    temp.next = b
                    b = b.next
                
                temp = temp.next

            while a is not None:
                temp.next = a
                a = a.next
                temp = temp.next

            while b is not None:
                temp.next = b
                b = b.next
                temp = temp.next

            return merged.next

        # case base
        if head == None or head.next == None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort1(head)
        right = self.merge_sort1(next_to_middle)

        sortedList = merge(left, right)

        return sortedList



linkedList = LinkedList(Node(100))
linkedList.append(Node(101))
linkedList.append(Node(110))
linkedList.append(Node(111))
linkedList.append(Node(1000))
linkedList.append(Node(1001))
linkedList.append(Node(1010))
linkedList.append(Node(1011))
linkedList.append(Node(1100))
linkedList.append(Node(1101))
linkedList.append(Node(1110))
linkedList.append(Node(1111))

linkedList.traverse()

len = linkedList.len()
TestCase().assertEqual(len, 12)
print(f'Lenght = {len}')

linkedList.append(Node(10000))
linkedList.append(Node(10001))
linkedList.append(Node(10010))
linkedList.append(Node(10011))
linkedList.append(Node(10100))
linkedList.append(Node(10101))
linkedList.append(Node(10110))
linkedList.append(Node(10111))
linkedList.append(Node(11000))
linkedList.append(Node(11001))
linkedList.append(Node(11010))
linkedList.append(Node(11011))
linkedList.append(Node(11100))
linkedList.append(Node(11101))
linkedList.append(Node(11110))
linkedList.append(Node(11111))

linkedList.traverse()
len = linkedList.len()
TestCase().assertEqual(len, 28)
print(f'Lenght = {len}')

print('==================== TEST PEEK METHOD ===================')
node = linkedList.peek(5)
print(f'Node {node.value} at position 5')
TestCase().assertEqual(node.value, 1000)

node = linkedList.peek(11)
print(f'Node {node.value} at position 11')
TestCase().assertEqual(node.value, 1110)

node = linkedList.peek(12)
print(f'Node {node.value} at position 12')
TestCase().assertEqual(node.value, 1111)

node = linkedList.peek(28)
print(f'Node {node.value} at position 28')
TestCase().assertEqual(node.value, 11111)
print('=========================================================')


print('==================== TEST INSERT METHOD ===================')

linkedList.insert(Node('a'), 5)
linkedList.insert(Node('a'), 5)
linkedList.insert(Node('b'), 10)
linkedList.insert(Node('c'), 32)
linkedList.traverse()

len = linkedList.len()
TestCase().assertEqual(len, 32)
print(f'Lenght = {len}')

node = linkedList.peek(5)
print(f'Node {node.value} at position 5')
TestCase().assertEqual(node.value, 'a')

node = linkedList.peek(32)
print(f'Node {node.value} at position 32')
TestCase().assertEqual(node.value, 'c')

print('=========================================================')

linkedList.delete('a')
linkedList.delete('a')
linkedList.delete('b')
linkedList.delete('c')
linkedList.traverse()


print('==================== TEST DELETE METHOD ===================')

len = linkedList.len()
TestCase().assertEqual(len, 28)
print(f'Lenght = {len}')

print('=========================================================')


print('==================== TEST GET MIDDLE METHOD ===================')

middleNode = linkedList.get_middle(linkedList.head)
TestCase().assertEqual(middleNode.value, 10001)
print(f'In the meddle position {14}, the node is {middleNode.value}')

print('=========================================================')


print('==================== TEST MERGE SORT METHOD ===================')

linkedList1 = LinkedList()
linkedList2 = LinkedList()

for i in range(500):
    linkedList1.append(Node(random.randint(1, 100000)))

linkedList1.merge_sort(linkedList1.head)
linkedList1.traverse()

print('=========================================================')

for i in range(100):
    linkedList2.append(Node(random.randint(1, 200)))

linkedList2.merge_sort1(linkedList2.head)
linkedList2.traverse()

print('=========================================================')