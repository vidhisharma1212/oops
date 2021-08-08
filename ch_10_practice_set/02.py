class Calculator:
    def __init__(self, number):
        self.number= number
    def square(self):
        print(f"square of {self.number} is {self.number**2}")
    def cube(self):
        print(f"cube of {self.number} is {self.number**3}")
    def squareRoot(self):
        print(f"square of {self.number} is {self.number**1/2}")

n= Calculator(4)
n.square()
n.cube()
n.squareRoot()