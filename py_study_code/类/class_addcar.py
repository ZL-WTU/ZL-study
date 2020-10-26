class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=20
    def get_descriptive_name(self):
        long_name=self.make+' '+self.model+' '+str(self.year)
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=milage
        else:
            print("You can't roll back an odometer")
    def increment_oometer(self,miles):
        self.odometer_reading+=miles