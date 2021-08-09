class Employee:
    salary= 1000
    increment= 1.5

    @property
    def salaryAfterIncrement(self):
       return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sa):
        self.increment= sa/self.salary

v= Employee()
print(v.salaryAfterIncrement)
print(v.increment)
v.salaryAfterIncrement= 2000
print(v.salaryAfterIncrement)
print(v.increment)