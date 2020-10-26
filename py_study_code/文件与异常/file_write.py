filename='programming.txt'
with open(filename,'a') as file_object: #open函数的第二个参数，‘w’写入模式（会覆盖原有内容）‘r’读取模式，‘a’附加模式（不会覆盖原有内容）
    file_object.write('I also love python\n')                       # ‘r+’读写模式,若省略第二个参数，编译器将默认以只读模式打开
    file_object.write('I also love program\n')                      #写入多行编译器不会自动换行，只有在写入时自己插入格式符号
                                                               # 若要写入的文件不存在，函数open将自动创建它（‘w’和‘a’都会）
                                                               #切记写入模式打开文件时，若文件已存在，编译器会在返回对象前清空原文件