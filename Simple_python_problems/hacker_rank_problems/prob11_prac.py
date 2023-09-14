arr = [1, 3, 4, 5, 6]
arr2 = [0]*8
print(arr2)

arr3 = [i for i in range(5)]
print(arr3)

l4 = list(i for i in range(1, 9))
print(l4)

print(set(map(str, l4)))

# 2d array #method1
row = []

for i in range(5):
    col = []
    for j in range(6):
        col.append(j)
    row.append(col)
for row in row:
    print(row)

# 2d array method2
# list comprehension

arr = [[i for i in range(4)] for j in range(3)]
print(arr)
