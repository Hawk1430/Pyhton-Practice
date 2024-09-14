class Shape:
    def __init__(self,color,isFilled):
        self.color = color
        self.isFilled = isFilled
        
    def describe(self):
        print(f"It is red and {"filled" if self.isFilled else "not filled"}.")
        
class Circle(Shape):
    def __init__(self,color,isFilled,radius):
        super().__init__(color,isFilled)
        self.radius = radius
        
        # Method overriding
        #
    def describe(self):
        print(f"It has an area of {3.14 * self.radius * self.radius} cm^2.")
        super().describe()
        
circle = Circle("red", True,5)
circle2 = Circle(color="Red",isFilled=True,radius=7)
circle.describe()
circle2.describe()
