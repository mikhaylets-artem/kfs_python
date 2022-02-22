class Shop:
    def __init__(self,shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def open_shop(self): 
        print(f"Ресторан открыт!")
    def describe_shop(self):
        print(f"{self.shop_name} {self.store_type}")
    def set_number_of_units(self):
        self.number_of_units=n
        print(self.number_of_units)
    def increment_number_of_units(self):
        self.number_of_units+=g
        print(self.number_of_units)
store=Shop("hjj","jkk")
store2=Shop("hjj2","jkk2")
n=int(input())
g=int(input())
