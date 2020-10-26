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
user_1=User("zhang",'san',"wuhan")
user_2=User("wang","wu","beijing")
user_3=User("li","si","nanjing")
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user() 