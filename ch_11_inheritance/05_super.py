class Person:
    country= "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    comapny="Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        print("I am an Employee and thus am breathing...")
    
class Programmer(Employee):
    comapany="Fiverr" 

    def getSalary(self):
        print("There is not salary")
    def takeBreath(self):
        super().takeBreath()
        print("I am breathing++...")

p= Person()
p.takeBreath()
e= Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()