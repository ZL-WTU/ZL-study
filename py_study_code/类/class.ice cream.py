class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())
    def open_restaurant(self):
        print(self.name+" is opening")
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors=['coco','cola','watermelon']
    def describe_ice_cream(self):
        for i in self.flavors:
            print(i)
IceCreamStand_1=IceCreamStand('KFC','IceCreamStand')
IceCreamStand_1.describe_ice_cream()