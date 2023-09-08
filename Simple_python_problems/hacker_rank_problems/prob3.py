class Person:
    def __init__(self, initAge):
        if initAge > 0:
            self.age = initAge
        else:
            print("Age is not valid setting age to zero '0'")
            self.age = 0

    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif (13 <= self.age < 18):
            print("You are teenager")
        else:
            print("You are old")

    def YearPasses(self):
        self.age = self.age+1


t = int(input())
for i in range(0, t):
    age = int(input("AGE: >"))
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.YearPasses()
    p.amIOld()
    print("")
