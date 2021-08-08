class Employee:
    company= 'Google'
    def getSalary(self):
        print(f"The salary of this person working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning Mam")
vid= Employee()
vid.greet()