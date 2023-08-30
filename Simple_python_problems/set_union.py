# practice your skills uncomment and run!


# # N = int(input())
# # A = set(map(int, input().split()))
# # M = int(input())
# # B = set(map(int, input().split()))
# # Newset = A.union(B)
# # print(len(Newset))


# # s = set("junaid")
# # s1 = set("Tariq")
# # print(s | s1)
# # print(s | set(["tariq"]))
# # print(s.union(enumerate(["t", "a", "r", "i", "q"])))

# # s = set()
# # print(s | set([1, 3]))
# # a = random.randint(1, 5)
# # list.append(str(a))
# # print(list)

# # seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # setb = {10, 1, 2, 3, 11, 21, 55, 6, 8}


# # print(len(seta) + len(setb-seta))

# # problem HackerCode
# '''The first line contains an integer, , the number of students who have subscribed to the English newspaper.
# The second line contains  space separated roll numbers of those students.
# The third line contains , the number of students who have subscribed to the French newspaper.
# The fourth line contains  space separated roll numbers of those students.'''

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# listb = [10, 1, 2, 3, 11, 21, 55, 6, 8]
# print(len(lista))
# listprint = ' '.join(str(i) for i in lista)
# print(listprint)
# set1 = set()
# for i in lista:
#     set1.add(i)

# print(len(listb))
# listprint = ' '.join(str(i) for i in listb)
# print(listprint)
# set2 = set()
# for i in listb:
#     set2.add(i)


# newset = set1 | set2
# print(len(newset))
# print(len(set1) + len(set2-set1))
# while len(set2) != n2:

#     for i in range(1, n2+1):
#         a = random.randint(1, n2)
#         set2.add(a)


# listprint = ' '.join(str(i) for i in set2)
# print(listprint)


n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

total = len(s1.union(s2))
print(total)
