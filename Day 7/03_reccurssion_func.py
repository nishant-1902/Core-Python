# recurssion is process its function call itself and its control by the condition
# formula : n * fac (n-1)
# 0! = 1
# 1! = 1
from math import factorial

def fact(n):
    if (n==1):
        return 1
    else:
        return (n * fact(n-1))
print(fact(3))