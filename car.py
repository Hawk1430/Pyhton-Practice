class Car:
    def __init__(self,brand,year,color,forSale):
        self.brand = brand 
        self.year = year
        self.color = color
        self.forSale = forSale
        
    def drive(self):
        print(f"You are driving {self.color} {self.brand}")
    
    def stop(self):
        print(f"You are stopping {self.color} {self.brand}")
        
    def description(self):
        print(f"The car is {self.brand} of {self.color} color of {self.year} and for sale its {self.forSale}")
        if self.forSale:
            print("Its for sale.")
        else:
            print("Its not for sale.")