class Programmar():
    def __init__(self, name, salary, address):
        self.name= name
        self.address= address
        self.salary= salary
        print("A new programmar is created!")

    def getDetails(self):
        print(f"Name of Programmar: {self.name} ")
        print(f"Salary of Programmar: {self.salary} ")
        print(f"Address of Programmar: {self.address} ")

vid= Programmar("Vidhi Sharma", '100 ', "Raipur")
vid.getDetails()
# rama= Programmar()
# vid.getDetails()