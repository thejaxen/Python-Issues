class Restaurant : 
    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"That {self.restaurant_name} has {self.cuisine_type} types.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open right now.")
    
    def served_customers(self):
        print(f"This restaurant served {self.number_served} orders.")
      
    def set_number_served(self,updated_number):
        self.number_served = updated_number
        
    def increment_number_served(self,increased_order):
        self.number_served += increased_order
              
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, flavors):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print(f"The available ice cream flavors at {self.restaurant_name} are:")
        for flavor in self.flavors:
            print(f"- {flavor}")