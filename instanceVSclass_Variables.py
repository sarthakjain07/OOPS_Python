class Student:
    # class variables
    grade=1
    no_of_students=0

    #constructor
    def __init__(self,name,roll,gender):
        # instance variables
        self.name=name
        self.roll=roll
        self.gender=gender
        self.grade=7
        Student.no_of_students+=1

    def newGrade(self):
        self.grade=self.grade+Student.grade    
        # self.grade=self.grade+self.grade  This is wrong as self.grade is instance variable  
print(Student.no_of_students)
Sarthak=Student("Sarthak",25,"Male")    
print(Student.no_of_students)
Neha=Student("Neha",26,"Female")
print(Student.no_of_students)



print(Sarthak.grade)    
Sarthak.newGrade()    
print(Sarthak.grade)    

# to print instance variables
print(Sarthak.__dict__)

# to print class variables
print(Student.__dict__)
        