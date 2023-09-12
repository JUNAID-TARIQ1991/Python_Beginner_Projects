# simple Dict
nam = {}
nam[0] = 'Junaid'
nam[1] = 'Zohaib'
nam[2] = 'Qudsia'
print(nam[2])
# update a dictionary
name1 = {1: 'Jumaid', 2: 'Zohaib'}
name1.update({3: 'Qudsia'})
print(name1)

# Add values to dictionary Using two lists of the same length
rollno = [4, 7, 9]
name = ['junaid', 'zohaib', 'Qudsia']
students = dict(zip(rollno, name))
print(students)

# Converting a list to the dictionary

names = ['junaid', 'zohaib', 'qudsia']
names = dict(enumerate(names))
print(names)

# getting dict key vlaue pair
name4 = {6: 'Junaid', 4: 'Zohaib', 5: 'Qudsia', 2: 'Tariq'}
for i in name4:
    print(i, name4[i])
# getting dict key vlaue pair using list coprehension
name5 = {5: 'Junaid', 1: 'Zohaib', 8: 'Qudsia', 2: 'Tariq'}
val = ''.join([(name5[i]) for i in name5])
print(val)
