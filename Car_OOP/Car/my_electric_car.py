from Car import ElectricCar
from Car import Battery


my_tesla = ElectricCar('tesla','model s',2018)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()