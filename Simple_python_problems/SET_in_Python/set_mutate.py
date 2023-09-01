set1 = {1, 4, 5, 6, 7, 8, 9, 0}
print(list(set1))
print(set1)
# add an element to set
set1.add(10)
print(set1)
print(len(set1))

set2 = {2, 4, 6, 8, 10, 12, 14}

print(set1 | set2)  # union
print(set1 ^ set2)  # summetric difference
print(set1 & set2)  # intersection
print(set1 - set2)

# this line of code use map function to convert each element of set to string and then converted to a list
# then we join each member of list with space ' ' using join function
new_set = ' '.join(i for i in list(map(str, set1)))
print(new_set)
