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


# Python 3 program to find the maximum
# sum of hour glass in a Matrix

# Fixing the size of the Matrix.
# Here it is of order 6 x 6

R = 5
C = 5

# Function to find the maximum sum of hour glass


def MaxSum(arr):

    # Considering the matrix also contains
    max_sum = -50000

    # Negative values , so initialized with
    # -50000. It can be any value but very
    # smaller.
    # max_sum=0 -> Initialize with 0 only if your
    # matrix elements are positive

    if (R < 3 or C < 3):
        print("Not possible")
        exit()

    # Here loop runs (R-2)*(C-2) times considering
    # different top left cells of hour glasses.
    for i in range(0, R-2):
        for j in range(0, C-2):

            # Considering arr[i][j] as top
            # left cell of hour glass.
            SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] +
                                                                                       arr[i + 2][j + 1] + arr[i + 2][j + 2])

            # If previous sum is less
            # then current sum then
            # update new sum in max_sum
            if (SUM > max_sum):
                max_sum = SUM
            else:
                continue

    return max_sum


# Driver Code
arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
res = MaxSum(arr)

print(f"Maximum sum of hour glass = {res}")

# This code is written by Akshay Prakash
# Code is modified by Susobhan Akhuli
