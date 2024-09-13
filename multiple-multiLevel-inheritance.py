class Animal():
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
        
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# multi level inheritance prey inherits animal and rabbit inherits prey

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


# multiple inheritance
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Jimmy")
hawk = Hawk("Baaz")
fish = Fish("Goldy")

print("------------")
rabbit.flee()
rabbit.eat()
rabbit.sleep()
print("------------")
hawk.hunt()
hawk.eat()
hawk.sleep()
print("------------")
fish.flee()
fish.hunt()
fish.eat()
fish.sleep()
print("------------")