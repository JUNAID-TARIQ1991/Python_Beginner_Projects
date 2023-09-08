n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i)
print(arr)
#converting to set
#s= set(map(int,arr))
#print(s)
arr.sort(reverse=False)
#str= [str(i) for i in arr]

num = ' '.join((i for i in list(str(i) for i in arr)))
print(num)