
# find the no repeative value from a list?S
set1 = {1, 4, 5, 6, 7, 8, 9, 0}

list1 = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3,
         2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

list2 = {}

for i in list1:
    if i in list2:
        list2[i] += 1
    else:
        list2[i] = 1
for i in list1:
    if list2[i] == 1:
        print(i)
