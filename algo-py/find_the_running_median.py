import heapq

def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers,-num)
    else:
        heapq.heappush(highers,num)
    
def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers,-heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers,-heapq.heappop(highers))

def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    lowers = []  # max heap, vals should go in and come out negated
    highers = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)
        result.append(round(getMedian(lowers, highers),1))
    return result

import bisect

def runningMedian1(a):
    p=[]
    l=0
    q=[]
    for i in range(len(a)):
        l=l+1
        bisect.insort(p,a[i])
        if(l%2==1):
            q.append(p[l//2])
        else:
            q.append((p[l//2]+p[l//2-1])/2)
    return q


a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(runningMedian1(a))