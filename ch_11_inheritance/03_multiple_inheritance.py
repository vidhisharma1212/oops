class Employee:
    company= "Visa"
    ecode= 120

class Freelancer:
    company="Fiverr"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee, Freelancer):
    name= "Sharma"

p= Programmer()
p.upgradeLevel()
print(p.level)
print(p.company) #visa is printed because Programmer(Employee, Freelancer), here, employee is written first so compnay on that class is given priority