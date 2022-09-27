class MyQueue(object):
    def __init__(self):
        self.mouth = []
        self.butt = []
    
    def peek(self):
        self.digest()
        return self.butt[-1]
        
    def pop(self):
        self.digest()
        return self.butt.pop()
        
    def push(self, value):
        self.mouth.append(value)
        
    def digest(self):
        if len(self.butt) == 0:
            while len(self.mouth) > 0:
                self.butt.append(self.mouth.pop())


# class MyQueue(object):
#     def __init__(self):
#         self.first_deque = deque()
#         self.second_deque = deque()
    
#     def peek(self):
        
#         FOR_MOST_LEFT_INDEX = 0
#         return self.first_deque[FOR_MOST_LEFT_INDEX]
        
#     def pop(self):
        
#         while self.first_deque:
#             self.second_deque.append(self.first_deque.pop())
        
#         first_value_from_stack = self.second_deque.pop()
        
#         while self.second_deque:
#             self.first_deque.append(self.second_deque.pop())
            
#         return first_value_from_stack
        
#     def push(self, value):
#         self.first_deque.append(value)


myQueue = MyQueue()

myQueue.push(10)
myQueue.push(20)
myQueue.push(30)
print(myQueue.peek())
print("")
pop_ = myQueue.pop()
print(pop_)

myQueue.pop()
myQueue.push(15)
print(myQueue.peek())
print("")
myQueue.pop()

myQueue.push(15)
print(myQueue.peek())
print("")
pop_ = myQueue.pop()
print(pop_)

