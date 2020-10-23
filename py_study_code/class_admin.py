class User():
    def __init__(self,fname,lname,location):
        self.fname=fname
        self.lname=lname
        self.location=location
    def describe_user(self):
        print('First name: '+self.fname,'Last name: '+self.lname)
        print('Location: '+self.location)
    def greet_user(self):
        print("Hello "+self.fname+" "+self.lname)
class Admin(User):
    def __init__(self,fname,lname,location):
        super().__init__(fname,lname,location)
        self.pricileges=['can add post','can delete post','can ban uesr']
    def show_privileges(self):
        for i in self.pricileges:
            print("The Admin "+i)
Admin_1=Admin('zhang','san','wuhan')
Admin_1.show_privileges()