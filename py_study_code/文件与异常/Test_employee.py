import unittest
from employee_class import Employee
class EmployeeTestCase(unittest.TestCase):
    def setUp(self):                                               #setUp()方法创建一个实例供后面测试使用，可以避免反复创造的麻烦
        self.fault=Employee('zhang','san',3000)
                                                                #setUp()方法创建实例时变量名前缀含‘self’（即存储在属性中）
    def test_give_default_raise(self):                          #因此可以在这个类的任何地方使用
        self.fault.give_raise()                                 #调用setUp()方法创建的实例类似C语言的结构体调用
        self.assertEqual(self.fault.money,8000)                 #要先‘。实例名’+实例所在类的对应方法

    def test_give_custom_raise(self):
        self.fault.give_raise(10000)
        self.assertEqual(self.fault.money,13000)


if __name__ == '__main__':
    unittest

