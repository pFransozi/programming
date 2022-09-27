'''
Ugly numbers are numbers whose only prime factors are 2, 3, 5.
First 11 ugly numbers are: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15

'''

def maxDivide(a, b):
    
    while a % b == 0:
        a = a / b
    
    return a

def isUgly(number):

    number = maxDivide(number, 2)
    number = maxDivide(number, 3)
    number = maxDivide(number, 5)

    return 1 if number == 1 else 0

def get_nth_ugly_number(number):

    i = 1
    count = 1
    
    while number > count:
        i += 1
        if isUgly(i):
            count += 1
    
    return i

number = get_nth_ugly_number(150)
print(f'150th ugly number is {number}')
