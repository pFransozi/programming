cache = {0:0, 1:1}

def fibonacci_with_recursion(n):
    #base cases
    if n <= 1: return n
    else: return fibonacci_with_recursion(n -1) + fibonacci_with_recursion(n - 2)

def fibonacci_with_cache_and_recursion(n):

    #base cases
    if n in cache: return cache[n]

    cache[n] = fibonacci_with_cache_and_recursion(n-1) \
                + fibonacci_with_cache_and_recursion(n-2) # recursion

    return cache[n]

def fib_bottom_up(n):

    # base case
    if n == 1 or n == 2: return 1

    bottom_up = [None] * (n + 1)
    bottom_up[0] = 0
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    
    
    return bottom_up[n]

    

#print(fibonacci_with_cache_and_recursion(999))
# print(fibonacci_with_recursion(10))
#print(fib_bottom_up(5))