'''
Implementation of a queue using a linkedList.

Main operations:

enqueue: insert an item in queue
dequeue: remove an item from queue

'''

class Node:

    def __init__(self, data, next=None) :
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
        return not self.next is None

class Queue:

    def __init__(self) -> None:
        self.front = None
        self.length = 0

    def enqueue(self, item:Node):
        
        #base case
        if self.length == 0:
            self.front = item
        else:
            current = self.front

            while current.next is not None:
                current = current.next
            
            current.next = item
        
        self.length += 1

    def dequeue(self) -> Node:
        
        #basic constraint
        if self.length == 0:
            raise ValueError("Queue is empty")
        else:
            tmp_front = self.front
            self.front = self.front.next
            self.length -= 1
            return tmp_front

queue = Queue()
queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(4))
queue.enqueue(Node(5))

print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)