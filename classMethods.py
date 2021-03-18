class Student:
    # class variables
    grade=1

    #constructor
    def __init__(self,name,roll,gender):
        # instance variables
        self.name=name
        self.roll=roll
        self.gender=gender
        self.grade=7

    # class method: when we use only class variables and not instance variables
    @classmethod
    def changeGrade(cls,newGrade):
        cls.grade=newGrade

    def newGrade(self):
        self.grade=self.grade+Student.grade

Sarthak=Student("Sarthak",25,"Male")
print(Sarthak.grade)
Sarthak.newGrade()            
print(Sarthak.grade)

Student.changeGrade(2)
Sarthak.newGrade()     
print(Sarthak.grade)
