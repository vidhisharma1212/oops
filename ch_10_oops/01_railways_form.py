class RailwayForm:
    formType= 'RailwayForm'
    def printData(self):
        print(f"Name is {self.name}") 
        print(f"Train is {self.train}")

myApllication = RailwayForm()
myApllication.name = input('Enter your name')
myApllication.train= 'Rajdhani Express'
myApllication.printData()