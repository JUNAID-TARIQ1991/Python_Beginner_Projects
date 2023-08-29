# Q: prompt user and get a integer number n and print on the terminal as 123....next
# i.e., n=3, ouput will be 123
# write the learninig outcome at the end
import string
# list1 = ["I", "Love", "My", "Son"]
list2 = []
n = int(input())
for i in range(1, n+1):
    list2.append(str(i))

print(list2)
toprint = ''.join([i for i in list2])
print(toprint)
