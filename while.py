prompt='\n please input something:'
prompt+='\n enter "quit" to end\n'
message=''
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)