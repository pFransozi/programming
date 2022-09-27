 
 
# from cmath import inf


# def cut_rod(price, n):

#     if n <= 0:
#         return 0

#     int max_val = -inf

#     for (i == 0; i < n; ++i):

        
    
#         max_val = INT_MIN
#         for j in range(i):
#             max_val = max(max_val, price[j] + val[i-j-1])
#             val[i] = max_val

#     return val[n]



# N = 8
# Price = [1, 5, 8, 9, 10, 17, 17, 20]

# result = cutRod(Price, N)


# def fibo_cal(n):

#     dynamic_process = [0 for _ in range(n)]
    
#     # 0, 1, 2 are base cases, from which the process begin.
#     dynamic_process[0] = 0
#     dynamic_process[1] = 1
#     dynamic_process[2] = 1

#     for idx in range(3, n):
#         dynamic_process[idx] = dynamic_process[idx - 1] + dynamic_process[idx - 2]

#     return dynamic_process

# print(fibo_cal(20))

import random

random_list = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]


print(random_list)