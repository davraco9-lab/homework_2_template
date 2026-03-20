class circle_class:
    # To initialize attributes 
    def __init__(self, radius):
        self.radius = radius  # Atributo de instancia

    # MEthods for the class
    def area(self):
        return self.radius*self.radius*3.1416
    
    def perimeter(self):
        return 2*3.1416*self.radius

