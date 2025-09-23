# 1] python is programming language length count
# 2] word < 3
# 3] ends with e
# 4] convert lower to upper and upper to lower

#1
# str = "python is programming language"
# a = len(str)
# print(a)

#2
str = "python is programming language"
word = str.split()
for i in word:
    if len(i) < 3:
        print("count the word length is less than 3 :",i)

#3
str = "python is programming language length"
word = str.split()
for j in word:
    if j[-1] == 'e':
        print("words ends with e : ",j)

#4
# str = "python is programming language length"
# a = str.swapcase()
# print(a)