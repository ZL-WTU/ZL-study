'''从模块导入函数的语法'''''
import module #导入整个模块
    module_name.function_name()#调用导入的模块中的具体函数

#导入特定的函数
'''直接使用函数名字调用即可）'''
from module_name import function_name
    #导入多个特定函数
        from module_name import function_name1,function_name2,function_name3

#使用as给函数指定别名
'''注意要在导入时使用'''
from module import function_name as XXX

#使用as给模块指定别名
'''在导入时使用'''
import module as XXX

#导入模块中的所有函数
'''使用“*”'''
from module import *