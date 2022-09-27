def swapArrayItems(arr, index_from, index_to, item_value):
    temp_value = arr[index_to]
    arr[index_to] = item_value
    arr[index_from] = temp_value

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    
    adjust_array_base = 1
    minimum_increase_count = 1
    
    count_min_swaps = 0
    index_arr = 0
    
    
    while index_arr < len(arr):

        item_arr = arr[index_arr]
        
        if item_arr != (index_arr + adjust_array_base):
            swapArrayItems(arr, index_arr, item_arr - adjust_array_base, item_arr)
            count_min_swaps += minimum_increase_count
        
        if arr[index_arr] == index_arr + 1:
            index_arr += 1
        
        
    return count_min_swaps

min = minimumSwaps([7, 1, 3, 2, 4, 5, 6])