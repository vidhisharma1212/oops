class Person:
    country= "India"

    def takeBreak(self):
        print("I am breathing...")

class Employee(Person):
    comapny="Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreak(self):
        print("I am an Employee and thus am breathing...")
    
class Programmer(Employee):
    comapany="Fiverr" 

    def getSalary(self):
        print("There is not salary")

p= Person()
e= Employee()
pr = Programmer()