# draw a triangle like given below
# You are given a positive integer  N. Print a numerical triangle of height N-1 like the one below:

# 1
# 22
# 333
# 4444
# 55555
# ......
# Can you solve it?

n = int(input())
list1 = []
for i in range(1, n):
    print(str(i)*i)
print("."*(n))
