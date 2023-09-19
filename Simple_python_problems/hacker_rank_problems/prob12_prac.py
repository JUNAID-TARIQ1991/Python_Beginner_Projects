class Person:
    def __init__(self, first_name, last_name, ID_number):
        self.first_name = first_name
        self.last_name = last_name
        self.ID_number = ID_number

    def printPerson(self):
        print("Name:", self.first_name, ", ",  self.last_name)
        print("ID:", self.ID_number)


class Student(Person):
    def __init__(self, score, first_name, last_name, ID):
        self.score = score
        super().__init__(first_name, last_name, ID)

    def calculate(self):
        # this line is vakid if you have only two element in a list
        # average = (self.score[0] + self.score[1])/2
        # for more the two elements
        average = sum(self.score)/len(self.score)
        print(average)
        if average <= 100 and average >= 90:
            return "O"
        elif average < 90 and average >= 80:
            return "E"
        elif average < 80 and average >= 70:
            return "A"
        elif average < 700 and average >= 55:
            return "P"
        elif average < 55 and average >= 40:
            return "D"
        else:
            return "T"


infoline = input("Enter your info here: "). split()
firstname = infoline[0]
lastname = infoline[1]
id = infoline[2]
numlist = list(map(int, input("Enter your score: ").split()))

s = Student(numlist, firstname, lastname, id)
s.printPerson()
print("Grade: ", s.calculate())
