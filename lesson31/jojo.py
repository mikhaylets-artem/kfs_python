class User:
    def __init__(self,first_name,last_name,age,year):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.year=year
        self.login_attemts=0
    def describe_user(self):
        print(f"First name : {self.first_name} Last name : {self.last_name} age : {self.age} year : {self.year}")
    def greeting_user(self):
        print(f"{self.first_name} {self.last_name} Hello ! ")
    def increment_login_attents(self):
        self.login_attemts+=1
        print(f"login attemts : {self.login_attemts}")
    def reset_login_attents(self):
        self.login_attemts=0
        print(f"login attemts : {self.login_attemts}")
class Admin(User):
    def __init__(self,first_name,last_name,age,year):
        super().__init__(first_name,last_name,age,year)
        self.privileges=["Allowed to add message","Allowed to delete users"]
        self.privileges=Privileges()
    
    def describe_admin(self):
        print("Information about the admin :")
        print(f"First name : {self.first_name} Last name : {self.last_name} age : {self.age} year : {self.year}")
    

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges=privileges
    def show_privileges(self):
        for privel in self.privileges:
            print(f"Administrator has these privileges : {privel}")

                
     
p1=User("Dana","Gen",17,2004)
p1.describe_user()
p1.greeting_user()

p1.increment_login_attents()
p1.increment_login_attents()

p1.reset_login_attents()
p1.increment_login_attents()

priv=Admin("Milen","Gem",19,2002)

priv.describe_admin()
priv.privileges.privileges = ["Allowed to add message","Allowed to delete users"]
priv.privileges.show_privileges()
