# recussion in Python: call same function inside the body of function
# converting decimal to binary using recursion

def dec_to_bin(n):
    if n > 1:
        dec_to_bin(n // 2)

    print(n % 2, end='')

# Decimal to binary using in-built function


def decimalToBinary(n):
    append(bin(n).replace("0b", ""))


# Driver Code
if __name__ == '__main__':

    # decimal value
    list1 = []
    n = int(input(">"))

    # Calling function
    dec_to_bin(n)
    print('\n', decimalToBinary(n))
    print(list1)


# problem solution
