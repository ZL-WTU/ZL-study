class Dog():                      #约定 类 的首字母大写   类中可以通过实例访问的变量称为属性（如下方的 name&age)
    def __init__(self,name,age):  #(1)init前后有两个_与普通方法以示区分
        self.name=name            #(2)此定义中self形参必不可少，且须位于首位，self让实例能够访问类中的属性和办法
        self.age=age              #(3)根据类创建实例传递形参时不用给self传递值

    def sit(self):                #此处不需要额外的信息，因此只有一个形参self
        print(self.name.title()+' is sitting ')
    def roll_over(self):          #同上
        print(self.name.title()+' rolled over')

my_dog=Dog("wangwang",6)
your_dog=Dog("hanhan",5)
print("My dog's name is "+my_dog.name)
print("My dog's age is "+str(my_dog.age))
my_dog.sit()                      #实例名称.方法    调用类中定义的方法
print("Your dog's name is "+your_dog.name)
print("Your dog's age is "+str(your_dog.age))
your_dog.roll_over()
