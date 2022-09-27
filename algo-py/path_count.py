def paths_count_recursive(row, col):

    if row == 1 or col == 1:
        return 1

    return paths_count_recursive(row - 1, col) + \
           paths_count_recursive(row, col - 1)


def paths_helper(row, col, lookup_table):
    
    #base condition
    if row == 1 or col == 1:
        return 1

    lookup_key = (row, col)

    if lookup_key in lookup_table:
        return lookup_table[lookup_key]
    
    recursive_result = paths_helper(row-1, col, lookup_table) + \
                       paths_helper(row, col-1, lookup_table)
    
    lookup_table[lookup_key] = recursive_result
    return recursive_result


def paths_count_recursive_with_memo(row, col):

    lookup_table = {}

    result = paths_helper(row, col, lookup_table)

    return result


def paths_count_dynamic_programming(row, col):
    
    subproblem = [0 for _ in range(col)]
    subproblem[0] = 1 # 

    for idx_row in range(0, row):
        for idx_col in range(1, col):

            subproblem[idx_col] += subproblem[idx_col-1]

    return subproblem[col-1]


print(paths_count_dynamic_programming(4, 4))
