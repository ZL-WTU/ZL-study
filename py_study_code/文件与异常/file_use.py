filename='pi_digits.txt'
with open(filename) as file_object:         #读取整个文件         #推荐使用with，让编译器决定什么时候关闭文件
    A=file_object.read()
    print(A)
print('\n')
with open(filename) as file_object:         #逐行遍历
    lines=file_object.readlines()           #readlines方法逐行读取文件每一行并将其存入一个列表中
    for line in lines:
        print(line.rstrip())
print('\n')
with open(filename) as file_object:        #with 模块外调用
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
print('\n')
with open(filename) as file_object:
    B=''
    C=file_object.readlines()
    for line in C:
        B+=line.strip()
    print(B.replace('a','d'))             #replace方法不会改变原字符串的内容
