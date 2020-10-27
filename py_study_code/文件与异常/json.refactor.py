import json         #所谓重构，即将代码划分为一系列完成具体工作的函数

def get_stored_username():
    '''如果存储了名字，就获取它'''
    filename='username.json'
    try:
        with open(filename) as f_ob:
            username = json.load(f_ob)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_uesename():
    '''提示用户输入用户名'''
    filename = 'username.json'
    username = input("Please input your name:\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    '''问候用户，并指出其名字'''
    filename = 'username.json'
    username = get_stored_username()
    if username:
        answer=input('Are you '+username+' ? yes/no\n')
        if answer=='yes':
            print("welcome come bcak " + username)
        else:
            username = get_new_uesename()
            print('We will remember you when you come back,' + username)
greet_user()