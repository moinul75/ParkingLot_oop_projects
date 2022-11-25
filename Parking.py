class Car:
    def __init__(self,licence, model,color) -> None:
        self.licence = licence
        self.model = model
        self.color = color
    def __repr__(self) -> str:
        return f"{self.licence},{self.model},{self.color}"
class Garadge:
    def __init__(self) -> None:
        self.add_car = []
        self.spot = 10
        self.car_info = {}
        self.ticket = {}
    def available_spot(self):
        return f"Total Spot={self.spot}"
    def adding_car(self,car):
        spotName = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1']
        if self.spot > 0:
            user_data = str(car).split(',')
            self.add_car.append(user_data)
            self.car_info = {'Ticket':[],'Licence':[],'Model':[],'Color':[]}
            ticket = ''
            for i,val in enumerate(self.add_car):
                ticket = spotName[i] + val[0]
                self.car_info['Ticket'].append(ticket)
                self.car_info['Licence'].append(val[0])
                self.car_info['Model'].append(val[1])
                self.car_info['Color'].append(val[2])
                self.spot -= 1
            print(f"Parked Successfully. Your Ticket is {ticket}")
    def Unparked(self,ticket,hours):
        if ticket not in self.car_info['Ticket']:
            print("NO CAR IS HERE")
            return 
        else:
            for i,val in enumerate(self.car_info['Ticket']):
                print("Car Serial number is: ",i)
                print(f"Your Ticket is {self.car_info['Ticket'][i]}")
                print(f"Your Licence is {self.car_info['Licence'][i]}")
                print(f"Your Model is {self.car_info['Model'][i]}")
                print(f"Your Color is {self.car_info['Color'][i]}")
                self.car_info['Ticket'].pop(i)
                self.car_info['Licence'].pop(i)
                self.car_info['Model'].pop(i)
                self.car_info['Color'].pop(i)
                self.spot += 1
        if hours > 5:
            print(f"TOTAL BILL= ${(hours * 5)+100}")
        else:
            print(f"TOTAL BILL= ${hours *5}")
    def total_car(self):
        for i in self.car_info.items():
            print(i)
gd = Garadge()
while True:
    print('='*10+"Parking Lot System"+'='*10)
    print("What do you want?")
    print("1.Parked Car\n2.Available Spot\n3.Unparked car\n4.Total car")
    choose = int(input("Enter the option your choose: "))
    if choose == 1:
        car_licence = input("Enter your car Licence: ")
        car_model = input("Enter your car model: ")
        car_color = input("Enter your car Color: ")
        user_input = Car(car_licence, car_model,car_color)
        gd.adding_car(user_input)
        print()
    elif choose == 2:
        print(gd.available_spot())
        print()
    elif choose == 3:
        ticket = input("Enter the ticket: ")
        hours = int(input("Enter hours of parked: "))
        if gd.spot == 10:
            print("NO CAR IS FOUND")
            continue
        else: 
           gd.Unparked(ticket, hours)
    elif choose == 4:
        gd.total_car()
        
    else:
        break
    
    
                
            
        

