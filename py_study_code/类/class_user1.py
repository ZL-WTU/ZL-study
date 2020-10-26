class User():
    def __init__(self,fname,lname,location):
        self.fname=fname
        self.lname=lname
        self.location=location
        self.login_attempts=0
    def describe_user(self):
        print('First name: '+self.fname,'Last name: '+self.lname)
        print('Location: '+self.location)
    def greet_user(self):
        print("Hello "+self.fname+" "+self.lname)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def pr_attempts(self):
        print(self.login_attempts)
user1=User("zhang","san","wuhan")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.pr_attempts()
user1.reset_login_attempts()
user1.pr_attempts()