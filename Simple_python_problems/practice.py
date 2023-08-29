import string


list = ["junaid", "tariq"]
a = ''.join(list)
print(a)

list = ["I", "Love", "to", "Travel"]
b = ','.join(list)
print(b)

list = ["I", "Love", "to", "Travel"]
a = ''.join([i for i in list])
print(a)

list = []
n = int(input())
for i in range(n):
    list.append(i)
print(list)
a = ''.join([i for i in list])
print(a)  # ???????  Why it is not working
