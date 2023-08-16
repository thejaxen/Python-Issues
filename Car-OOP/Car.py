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

