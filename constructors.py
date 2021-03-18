class Student:
    # constructor in python
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    # self made function also take one argument named self
    def printInfo(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)

Sarthak=Student("Sarthak",25,96.2)
Sarthak.printInfo()