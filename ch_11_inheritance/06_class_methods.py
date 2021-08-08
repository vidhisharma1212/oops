class Employee:
    campany="camel"
    salary= 100
    location= "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary= sal

    @classmethod
    def changeSalary(self, sal):
         self.salary= sal

e= Employee()
print(e.salary)

e.changeSalary(300)
print(e.salary)

print(Employee.salary)

