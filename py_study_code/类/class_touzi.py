from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))
def roll_10(die):
    for i in range(0,10):
        die.roll_die()
    print("-----------")
die=Die()
roll_10(die)
die=Die(10)
roll_10(die)
die=Die(20)
roll_10(die)