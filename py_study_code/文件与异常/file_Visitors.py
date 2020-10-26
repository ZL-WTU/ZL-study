userbook='userbook.txt'
while True:
    name = input('Enter your name:')
    if name=='quit':
        break
    else:
        print("hello "+name)
        with open(userbook,'a') as usb:
            usb.write(name+' has login\n')