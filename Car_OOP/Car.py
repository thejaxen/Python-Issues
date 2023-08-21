class Car:
    
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 30 
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
        
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")
            
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self,battery_size):
        if self.battery_size < 100 :
            self.battery_size = 100
            print(f"Battery size upgraded to {self.battery_size}.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")        


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__( make, model, year)
        self.battery = Battery()
        
#Defining Attributes and Methods for the Child Class        

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
#Overriding Methods from the Parent Class

    def fill_gas_tank(self):
        print("This car does not need a gas tank!")

print('This is the new part as Instances as Attributes')
my_tesla = ElectricCar('tesla','model s',2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

