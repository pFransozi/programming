'''

Selection sort is an in-place comparison sorting algorithm. It has an O(n^2) time complexity, 
which makes it inefficient on large lists, and generally performs worse than the
similar insertion sort. It is a brute force algorithm.

'''
from unittest import TestCase

def find_min(list_):

    min_index = 0
    
    for i in range(len(list_)): #O(n)

        if list_[i] < list_[min_index]:
            min_index = i
    
    return list_[min_index]

def selection_sort(list_):

    for i in range(len(list_) - 1): # the worst case it is O(n^2)

        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        
        list_[i], list_[min_index] = list_[min_index], list_[i]


    
TestCase().assertEqual(find_min([1, 7, 8, 9, 0]), 0)
TestCase().assertEqual(find_min([1, 7, -1, 8, 9, 0]), -1)

test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
test_list_expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
selection_sort(test_list)
TestCase().assertEqual(test_list, test_list_expected)