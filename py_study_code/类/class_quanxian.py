class Privileges():
    def __init__(self):
        self.pricileges = ['can add post', 'can delete post', 'can ban uesr']
    def show_privileges(self):
        for i in self.pricileges:
            print("The Admin "+i)
class Admin():
    def __init__(self):
        self.pricileges=Privileges()
Admin1=Admin()
Admin1.pricileges.show_privileges()