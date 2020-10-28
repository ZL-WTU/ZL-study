class Employee():
    def __init__(self, firname, lasname, money):
        self.firname = firname
        self.lasname = lasname
        self.money = money

    def give_raise(self, num=5000):
        self.money += num
