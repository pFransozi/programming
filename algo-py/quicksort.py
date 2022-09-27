'''

'''
import random

def partition(list_, start, end):

    pivot = list_[end]
    i = start - 1

    for j in range(start, end):
        
        if list_[j] <= pivot:

            i = i + 1
            list_[i], list_[j] = list_[j], list_[i]

    list_[i + 1], list_[end] = list_[end], list_[i + 1]

    return i + 1


def quick_sort(list_, start, end):
    
    if start >= end:
        return

    #
    p = partition(list_, start, end)

    quick_sort(list_, start, p-1) # left side
    quick_sort(list_, p+1, end) # right side


data = [random.randint(0, 1000000) for _ in range(200000)]
print('Unsorted data: {0}'.format(data))

quick_sort(data, 0, len(data)-1)

print('Sorted data: {0}'.format(data))