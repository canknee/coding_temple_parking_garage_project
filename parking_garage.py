class ParkingGarage():
    MAXCAPACITY = 6

    def __init__(self):
        self.parkingSpaces = [1, 2, 3, 4, 5, 6]
        self.ticketcounter = 0
        self.currentTicket = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True}

    def takeTicket(self):
        self.ticketcounter += 1
        self.parkingSpaces.pop()
        takenspot = self.parkingSpaces.pop()
        self.currentTicket[takenspot] = False
        print(takenspot)


    # def payForParking(self): 


    # def leaveGarage(self):


    # def exitGarage():


def garage():
    action = input("Welcome to the parking garage. You can: Take a ticket(Take), Pay, Leave, or Quit ") 
    if action.lower() == "take":
        ParkingGarage.takeTicket()


car = ParkingGarage()
garage()