import random

def partition(list_, start, end):
    
    pivot = list_[end]
    swap_idx = start - 1

    for index in range(start, end):

        if list_[index] <= pivot:
            
            swap_idx += 1 # change swap index to the new position
            list_[index], list_[swap_idx] = list_[swap_idx], list_[index]
    
    
    swap_idx += 1 # change the pivot. the pivot is moved next to the last element that is less than it.
    list_[swap_idx], list_[end] = list_[end], list_[swap_idx]
    
    return swap_idx



def quick_sort(list_, start, end):

    if start > end: return


    pivot = partition(list_, start, end)

    quick_sort(list_, start, pivot-1) # left
    quick_sort(list_, pivot+1, end ) # right



data = [ random.randint(0, 300) for _ in range(20) ]

print(data)

quick_sort(data, 0, len(data) - 1)
print(data)