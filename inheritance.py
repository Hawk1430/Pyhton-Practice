class Animal():
    def __init__(self,name):
        self.name = name
        self.isAlive = True
    
    def walk(self):
        print(f"{self.name}n is walking")

class Dog(Animal):
    def voice(self):
        print(f"{self.name}   is barking")
        
dog = Dog("Jimmy")

dog.walk()
dog.voice()