class ParkingGarage():
    MAXCAPACITY = 6

    def __init__(self, capacity):
        self.parkingSpaces = [i for i in range(1, capacity+1)]
        self.ticketcounter = 0
        self.currentTicket = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True}

    def takeTicket(self):
        if len(self.parkingSpaces) > 6:
            print("Lot is full, sry")
        if self.parkingSpaces == []:
            print("Lot is full, sry")
        else:
            self.ticketcounter += 1
            takenspot = self.parkingSpaces.pop(0)
            self.currentTicket[takenspot] = False
            print(f"You have ticket number: {takenspot}. Please pull forward to your assigned spot")
            print("There are " + str(len(self.parkingSpaces)) + " parking spaces left")

    def payForParking(self): 
        ticketnumber = input("Please enter your ticket number: ")
        print("Your total is $15.00")
        payment = input("Please enter the amount you would like to pay: ")
        if not payment.isdigit():
            print("Please enter a valid number")
        elif int(payment) > 15:
            self.currentTicket[ticketnumber] = True
            print("Here is your change:" + str(int(payment)-15))
        elif int(payment) == 15:
            self.currentTicket[ticketnumber] = True
            print("Thanks, you have 15 minutes to leave")
        elif int(payment) < 15:
            print("You still owe: " + str(15-(int(payment))))
            remainder = 15-(int(payment))
            remainderinput = input("Please pay the remainder ")
            if int(remainderinput) == remainder:
                print("Thanks you have 15 minutes to leave")
            else:
                print("I'll see your ass in court")
# above and beyond  :  we create another class specifically for ticket including ticket price, remainder, etc.
# you would have to instantiate the ticket object
# or you can assign tickets to a dictionary - 

    def leaveGarage(self):
        ticketnumber = int(input("Please enter the ticket number you paid for: "))
        if self.currentTicket[ticketnumber] == False:
            print("Please pay for your ticket")
        if self.currentTicket[ticketnumber] == True:
            print("Thank you, have a nice day. ")
            self.parkingSpaces.insert(ticketnumber-1, ticketnumber)

    def garageSales(self):
        print(self.ticketcounter)

def garage():
    while True:
        empty = True
        for v in car.currentTicket.values():
            if v == False:
                empty = False
        action = input("Welcome to the parking garage. You can: Take a ticket(Take), Pay, Leave, or Quit ") 
        if action.lower() == "take":
            car.takeTicket()
        if action.lower() == "pay":
            if empty:
                print("Lol thanks for the free money")
            else:
                car.payForParking()
        if action.lower() == "leave":
            if empty:
                print("cya later...but how did you get in here...?")
            else:
                car.leaveGarage()
        if action.lower() == "quit":
            break
        if action.lower() == "sales":
            car.garageSales()


car = ParkingGarage(6)
garage()