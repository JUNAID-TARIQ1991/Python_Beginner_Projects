n= int(input())
arr= []
while len(arr) <n:
    arr.append(int(input()))

def list_reverse(arr,n):
 
    #if only one element present, then return the array
    if(n==1):
        return arr
     
    #if only two elements present, then swap both the numbers.
    elif(n==2):
        arr[0],arr[1],=arr[1],arr[0]
        return arr
     
    #if more than two elements presents, then swap first and last numbers.
    else:
        i=0
        while(i<n//2):
 
    #swap present and preceding numbers at time and jump to second element after swap
            arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
       
    #skip if present and preceding numbers indexes are same
            if((i!=i+1 and n-i-1 != n-i-2) and (i!=n-i-2 and n-i-1!=i+1)):
                arr[i+1],arr[n-i-2]=arr[n-i-2],arr[i+1]
            i+=2
        return arr
rev_list=list_reverse(arr,n)
num = ' '.join(i for i in list(map(str,rev_list)))

print(num)

''' Explanation!
This Python code takes an integer n as input, which represents the number of elements in a list arr. It then reads n integers from the user and stores them in the arr list. After that, it defines a function list_reverse that is used to reverse the elements of the list according to a specific pattern. Finally, it prints the reversed list as a space-separated string.

Here's a step-by-step explanation of the code:

n = int(input()): Reads an integer n from the user, which represents the number of elements in the list.

arr = []: Initializes an empty list arr to store the input elements.

while len(arr) < n:: This loop continues until the length of the arr list is equal to n. It reads integers from the user and appends them to the arr list.

def list_reverse(arr, n):: Defines a function called list_reverse that takes two arguments: arr (the list to be reversed) and n (the number of elements in the list).

Inside the function:

if n == 1:: Checks if there is only one element in the list. If so, it returns the list as it is because there is no need to reverse a single-element list.

elif n == 2:: Checks if there are only two elements in the list. If so, it swaps the positions of the two elements and returns the modified list.

Otherwise (if there are more than two elements):

It uses a while loop to reverse the list elements in a specific pattern:
It starts with i = 0 and continues while i < n // 2, which means it iterates through the first half of the list.
In each iteration, it swaps the element at index i with the element at index n - i - 1. This effectively reverses the first and last elements.
It also checks if i and n - i - 1 are not adjacent elements (i.e., the indices are not (i, i+1) and (n-i-1, n-i-2)) and swaps them as well. This handles reversing the elements in a non-adjacent pattern.
The loop increments i by 2 in each iteration to jump to the next pair of elements to be swapped.
After the loop, it returns the modified list.
rev_list = list_reverse(arr, n): Calls the list_reverse function with the input list arr and the number of elements n, and stores the reversed list in the variable rev_list.

num = ' '.join(i for i in list(map(str, rev_list))): Converts the elements of the rev_list to strings using map(str, rev_list), then joins them into a single string separated by spaces.

print(num): Prints the resulting string, which represents the reversed list.

'''