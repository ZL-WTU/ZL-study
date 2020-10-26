import json                                                     #json模块用于存储数据
filename='username.json'
try:
    with open(filename) as f_ob:
        name = json.load(f_ob)                                  #json.load 将文件中的数据读取到内存中
except:
    username=input("Please input your name:\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)                              #json.dump 接受两个实参:要存储的数据以及可用于存储数据的文件对象
        print('We will remember you when you come back,' + username)
else:
    print("welcome come bcak "+name)