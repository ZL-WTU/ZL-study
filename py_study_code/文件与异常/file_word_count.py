def count_words(filename):
    try:                                                        #try后面放可能引发异常的模块
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:                                   #except跟异常名称和出现该异常后将执行的代码
        print("sorry the file "+filename+" does not exist")
    else:                                 #else后面放没有出现except指出的异常后将运行的代码（没有except所指出的异常会跳过except模块）
        words=contents.split()            #split方法以空格为分隔符将字符串拆分为多个部分并存储到一个列表当中
        number=len(words)
        print('The file '+filename+ ' has about '+str(number)+' words')
filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

