# A = {1, 2, 3, 5, 6}
# B = {9, 8, 5, 6, 3, 2, 1, 4, 7}
# D = {1, 3, 4, 5, 6, 7, 8}
# c = A & B
# test = (c - A)
# if test == set():
#     print(True)

# # 0r
# print(A.issubset(B))

A = set(map(int, input().split()))
is_sset = True
for i in range(int(input())):
    n1 = set(map(int, input().split()))
    if len(n1) < 21 and len(A) < 501:
        if not A.issuperset(n1):
            is_sset = False

print(is_sset)
