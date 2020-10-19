def make_car(maker,size,**infos):
    car_info={}
    car_info['maker']=maker
    car_info['size']=size
    for k,v in infos.items():
        car_info[k]=v
    return  car_info
car=make_car('subaru','outback',color="blue",tow_package=True)
print(car)