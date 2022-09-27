'''

This priority queue is based on the python list and it uses the heapq, also known as the priority queue algorithm. 
In a priority queue, an element with high priority is served before an element with low priority. 

'''

import heapq


class PriorityQueue:
    
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self) -> str:
        return str(self.elements)

if __name__ == '__main__':
    pQueue = PriorityQueue()

    print(pQueue)
    
    pQueue.put('eat', 2)
    pQueue.put('code', 1)
    pQueue.put('sleep', 3)
    pQueue.put('nap', 4)
    pQueue.put('work', -1)


    print(pQueue)
    print(pQueue.get())
    print(pQueue)
