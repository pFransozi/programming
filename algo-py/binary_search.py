'''
It is a very efficient algorithm with the worst time complexity as O(log n).

Two ways to implement binary search: recursive and dynamic. Remember the call memory cost when
use recursive technique.
'''

def binary_search_recursive(list, start_index, end_index, target):

    mid_index = start_index + (end_index - start_index) // 2

    if (start_index > end_index):
        return -1
    if list[mid_index] == target:
        return mid_index

    if target < list[mid_index]:         
        return binary_search_recursive(list, start_index, mid_index - 1, target)
    else:
        return binary_search_recursive(list, mid_index + 1, end_index, target)

def binary_search_dynamically(list, target):

    low_pointer = 0
    high_pointer = len(list) -1

    while low_pointer <= high_pointer:

        mid_pointer = low_pointer + (high_pointer - low_pointer) // 2

        if target == list[mid_pointer]:   return mid_pointer
        elif target <= list[mid_pointer]: high_pointer = mid_pointer -1
        elif target > list[mid_pointer]: low_pointer = mid_pointer + 1
    

personal_code = [x for x in range(400_000)]

print(binary_search_recursive(personal_code, 0, len(personal_code) - 1, 302))

print(binary_search_dynamically(personal_code, 302))