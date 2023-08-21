class User :
    
    def __init__(self,first_name,last_name,login_attempts) :
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 12
        
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}.")
        
    def greet_user(self):
        print(f"Congrats user {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self,increased_number):
        self.login_attempts += increased_number 
        print(f"This user logined {self.login_attempts} times.")              
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"This users login attempts are {self.login_attempts} right now.")

class Admin(User): 
    
    def __init__(self,first_name,last_name,login_attempts,privileges):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges = privileges
        
    def show_privileges(self):
        for settings in self.privileges:
            print(settings)

class Privileges:
    
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges

    def print_privileges(self):
        print(f"{self.privileges}")
        
        