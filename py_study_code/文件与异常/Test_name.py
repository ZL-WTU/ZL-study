import unittest                                             #导入测试模块
from name import get_fotrmatted_name                        #导入要测试的函数

class NameTestCas(unittest.TestCase):                      #创建测试类，注意要继承unittest.TestCase类，类名自定义但要包含‘Test’
    '''测试name.py'''
    def test_first_last_name(self):                        #定义测试方法，必须以‘test_’开头，编译器将自动运行'test_'打头的方法
        '''能够正确处理像 Janis Joplin这样的姓名吗？'''
        fomatted_name=get_fotrmatted_name('janis','joplin')
        self.assertEqual(fomatted_name,'Janis Joplin')    #断言方法assertEqual(),意思是将formatted_name字符串与‘Janis Joplin’
                                                         #比对，如果完全相等则测试通过


if __name__ == '__main__':              #这个其实就是一种写python的良好的习惯，如果你在一个python文件A中，添加了这个语句，
    # 然后你把python文件A导入到pyhton文件B里面，如果pythonB 里面有和python文件A中同名的函数C，
    # 在运行文件B的时候，只会执行B中的函数C而不会执行文件A中的函数C！如果没有这一天语句，那么文件A和B中的函数都会被执行！

    unittest

