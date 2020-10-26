filename='alice.txt'
with open(filename) as book:
    line=book.read()                        #将文件转为字符串
    print(line.lower().count('the'))        #lower将字符串转换为小写，可捕捉到要查找的单次出现的所有次数，count方法确定目标单次出现次数
