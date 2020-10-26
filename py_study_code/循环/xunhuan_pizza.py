prompt='\nplease input toppings:'
prompt+='\nenter "quit"to end\n'
message=''
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print('we will add '+message)
    else:
        break