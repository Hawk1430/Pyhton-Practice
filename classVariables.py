class Student:
    # class variables
    classYear = 2024
    numOfStudents = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.numOfStudents += 1
        
    # As this not take any input so it will be called using class name only
    def strength():
        print(f"The total strength is {Student.numOfStudents}")    
    
    # Take iput so will be called only using the object name
    def details(self):
        print(f"{self.name}'s age is {self.age}")

student1 = Student("Rohan",17)

student1.details()
Student.strength()