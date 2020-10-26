catnames='cats.txt'
dognames='dogs.txt'
try:
    with open(catnames) as ca:
        ca_names = ca.read()
        print(ca_names)
    print("\n")
    with open(dognames) as do:
        do_names = do.read()
        print(do_names)
except FileNotFoundError:
    print('The file does not exist')        #except模块用pass可以让编译器对该指定异常”一言不发“
