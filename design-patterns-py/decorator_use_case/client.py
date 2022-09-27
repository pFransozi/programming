from value import Value
from add import Add
from sub import Sub

A = Value(1)
B = Value(2)
C = Value(5)

print(Add(A, B))
print(Add(A, 100))
print(Sub(C, A))
print(Sub(Add(C, A), A))
print(Sub(100, 101))
