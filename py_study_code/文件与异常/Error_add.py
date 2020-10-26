while True:
    first_number=input('\nEnter first number or enter q to end:')
    if first_number=='q':
        break
    second_number=input('\nEnter second number or enter q to end:')
    if second_number=='q':
        break
    try:
        result=int(first_number)+int(second_number)
    except ValueError:
        print("请输入数字")
    else:
        print(result)