def insertion(data_list, index):
    
    key_value = data_list[index]
    idx_sublist = index - 1

    while idx_sublist >= 0 and key_value < data_list[idx_sublist]:
        data_list [idx_sublist + 1] = data_list[idx_sublist]
        idx_sublist -= 1

    data_list [idx_sublist + 1] = key_value

def insertion_sort(data_list):

    len_data_list = len(data_list)
    
    # constraint
    if len_data_list <= 1:
        return data_list

    
    for idx in range(1, len_data_list):

        insertion(data_list, idx)


data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(data)

insertion_sort(data)
print(data)