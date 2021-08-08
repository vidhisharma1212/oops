class Employee:
    company= 'Google'
    def getSalary(self, signature,address):
        print(f"The salary of this person working in {self.company} is {self.salary} \n{signature}\n{address}")

vid= Employee()
vid.salary= 1000
# vid.getSalary()  # Employee.getSalary(vid)

vid.getSalary("Thanks", "Raipur")