import json

filename='number.json'
try:
    with open(filename) as f_obj:
        a=json.load(f_obj)
        print("i konw the number is "+a)
except:
    number = input('enter your favorite number:\n')
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
