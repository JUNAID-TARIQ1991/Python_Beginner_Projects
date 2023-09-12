
# https://www.geeksforgeeks.org/python-reversing-list/

n = int(input())
arr = []
while len(arr) < n:
    arr.append(int(input()))


def list_reverse(arr, n):

    # if only one element present, then return the array
    if (n == 1):
        return arr

    # if only two elements present, then swap both the numbers.
    elif (n == 2):
        arr[0], arr[1], = arr[1], arr[0]
        return arr

    # if more than two elements presents, then swap first and last numbers.
    else:
        i = 0
        while (i < n//2):

            # swap present and preceding numbers at time and jump to second element after swap
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    # skip if present and preceding numbers indexes are same
            if ((i != i+1 and n-i-1 != n-i-2) and (i != n-i-2 and n-i-1 != i+1)):
                arr[i+1], arr[n-i-2] = arr[n-i-2], arr[i+1]
            i += 2
        return arr


rev_list = list_reverse(arr, n)
num = ' '.join(i for i in list(map(str, rev_list)))

print(num)
