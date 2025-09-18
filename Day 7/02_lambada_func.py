# syntax : lambada arguments : expression
total = lambda n1,n2 : n1 + n2
print(total(10,20))

even = lambda num1 : num1 % 2 == 0
print(even(2))

l = (1,2,3,4,5,6,5,7,8)
newlist = list(filter(lambda n1:n1 % 2 == 0,l))
print(newlist)

newlist1 = list(map(lambda n1:n1*n1,l))
print(newlist1)
    