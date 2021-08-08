class Employee:
    comapny= "Bharat Gas"
    salary= 5600
    salaryBonus= 500

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus= val- self.salary

e= Employee()
print(e.totalSalary)

e.totalSalary=5800
print(e.salaryBonus)
print(e.salary)