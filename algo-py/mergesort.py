'''

Do not forget: O(n logn), the recursive part of the algorithm is O(log n) because split 
the list by two (divide and conquer method), and when the algorithm compares each side of the list of the other, 
that is O(n).

'''

import random

def merge_sort(unsorted_list):

    if len(unsorted_list) < 2:
        return unsorted_list

    middle_index = len(unsorted_list) // 2
    left_side_list = unsorted_list[0:middle_index]
    right_side_list = unsorted_list[middle_index::]

    return merge(merge_sort(left_side_list), merge_sort(right_side_list))

def merge(left_side_list, right_side_list):

    result_list = []
    left_index = 0
    right_index = 0

    while(left_index < len(left_side_list) and right_index < len(right_side_list)):

        if left_side_list[left_index] < right_side_list[right_index]:
            result_list.append(left_side_list[left_index])
            left_index = left_index + 1
        else:
            result_list.append(right_side_list[right_index])
            right_index = right_index + 1

    for remain_item in left_side_list[left_index::]:
        result_list.append(remain_item)
    
    for remain_item in right_side_list[right_index::]:
        result_list.append(remain_item)

    return result_list


data = [random.randint(0, 200000) for _ in range(200000)]

print(merge_sort(data))



