class Train:
    def __init__(self, name,fare, seats ):
        self.fare= fare
        self.seats= seats
        self.name= name
    def getInfo(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are : {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is : Rs {self.fare}")
    def bookTicket(self):
        question= int(input("Enter the number of seats you want to book on the train."))
        if(self.seats>0):
            if question>1:
                print(f"Your ticket has been booked! Your seat number is from {self.seats-question} to {self.seats}")
               
            else:
                print(f"Your ticket has been booked! Your seat number is {self.seats}")
            print(f"Your total bill is : {90*question}")
            self.seats= self.seats- question
            p= True
            p= input("Want to book more tickets?")
intercity= Train("Intercity Express : 14015", 90, 300)
intercity.getInfo()
ask= True
while ask!="exit" or p=='yes':
    ask= input("Do you want to book a ticket of this train? : \n")
    if ask.lower()=='yes':
        intercity.fareInfo()
        print("Please type yes to continue\n")
        cont= input("Type : \n")
        if cont=="yes":
            intercity.bookTicket()     
        else:
            exit()
    elif ask.lower()=='no':
        print("Okay")
        exit()
    else:
        print("Please respond in either yes, no or exit")