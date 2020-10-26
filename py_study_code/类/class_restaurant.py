class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())
    def open_restaurant(self):
        print(self.name+" is opening")
restaurant=Restaurant("HongRi","China")
restaurant_1=Restaurant("KFC","Fast")
restaurant_2=Restaurant("BAFANG","Hot pot")
restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()