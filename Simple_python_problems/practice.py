import string

# using join

list = ["junaid", "tariq"]
a = ''.join(list)
print(a)

list = ["I", "Love", "to", "Travel"]
b = ','.join(list)
print(b)

list = ["I", "Love", "to", "Travel"]
a = ''.join([i for i in list])
print(a)

# list = []
# n = int(input())
# for i in range(n):
#     list.append(str(i))
# print(list)
# a = ''.join([i for i in list])
# print(a)


# map function:
list3 = ["I", "am", 22, "year", "old"]
list_to_str = ''.join(map(str, list3))
print(list_to_str)

# enumerate function
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

listToStr = '-'.join([str(elem) for i, elem in enumerate(s)])

listToStr1 = ','.join([str(elem) for i, elem in enumerate(s)])

print(listToStr)
print(listToStr1)
