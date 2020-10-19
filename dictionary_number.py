like_numbers={'zhangsan':[4,5,11],'wangwu':[13,56,99],'lixaing':[22,88,12]}
for k,v in like_numbers.items():
    print('\n'+k.title()+"  likes:")
    for num in v:
        print(num)