class Employee:
    company= 'Google'

    def __init__(self, name, salary, subunit):
        self.name= name
        self.salary= salary 
        self.subunit= subunit
        print("Employee is created ! ")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")        
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getSalary(self):
        print(f"The salary of this person working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning Mam")

vid= Employee('vidhi','100','YouTube')
# vid=Employee() this throws an error of missing 3 arguments
vid= Employee(pass, pass ,pass )
vid.getDetails()
print(vid.salary)