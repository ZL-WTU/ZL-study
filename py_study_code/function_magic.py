def show_magicians(names):
    for name in names:
        print(name)
def make_great(names,c_names):
    for i in range(len(names)):
        names[i] = 'the great ' + names[i] #要修改列表的值需要具体的索引
        c_names.append(names[i])
magicians=['zhangsan','wangwu','lisi']
changed=[]
make_great(magicians[:],changed) #用切片传递列表，被修改的是副本
show_magicians(magicians)
show_magicians(changed)