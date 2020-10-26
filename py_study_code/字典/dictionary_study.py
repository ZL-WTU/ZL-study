favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
check_names={'wangwu','zhangsan','jen','phil'}
for name in check_names:
    if name in favorite_language.keys():
        print(name+",thanks")
    else:
        print(name+', please')
