class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number=3
    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())
    def open_restaurant(self):
        print(self.name+" is opening")
    def read_number(self):
        print("There had "+str(self.number))
    def set_number_served(self,num):
        self.number+=num
restaurant=Restaurant("Hongri","china")
restaurant.set_number_served(15)
restaurant.read_number()