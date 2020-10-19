current_names=["lihua","zhangsan","xiaoming","wangqiang","admin"]
new_users=["ZHangsan","wangwu","xiaoming"]
for new_user in new_users:
    a=new_user
    if a.lower() in current_names:
        print(new_user+" had")
    else:
        print(new_user+" can be used")

