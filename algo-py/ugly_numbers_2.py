def nthUglyNumber(n):
     
    # Base cases...
    if (n == 1 or n == 2 or n == 3 or n == 4 or n == 5):
        return n
    s = [1]
    n-=1
 
    while (n):
        it = s[0]
         
        # Get the beginning element of the set
        x = it
         
        # Deleting the ith element
        s = s[1:]
        s = set(s)
         
        # Inserting all the other options
        s.add(x * 2)
        s.add(x * 3)
        s.add(x * 5)
        s = list(s)
        s.sort()
        n -= 1
    # The top of the set represents the nth ugly number
    return s[0]
 
# Driver Code
n = 150
 
# Function call
print( nthUglyNumber(n))