responses={}
active=True
while active:
    name=input('your name: ')
    response=input('which one do you like? \n')
    #input()将键入的变量存储为字符串类型
    #将回答存入字典
    responses[name]=response
    repeat=input('anyone else?(yes/no)\n')
    if repeat=='no':
        active=False
print('There are the results:\n')
for name,response in responses.items():
    print(name+' like '+response)