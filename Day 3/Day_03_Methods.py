fruits = [1,2,3,"mango","apple","apple"]
fruits.append("orange")
print(fruits) # append object method

fruits2 = ["grapes",3,45,7]
fruits.append(fruits2)
print(fruits) # append list

fruits2.clear()
print(fruits2)  # clear list

x = fruits.copy()
print(x)

g = fruits.count("apple")
print(g) # count

h = fruits.index("mango")
print(h) # index

