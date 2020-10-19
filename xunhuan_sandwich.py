sandwich_orders=['tuna','pastrami','huotui','pastrami','tomato','pastrami']
finished_sandwiches=[]
print('pastrami is soldout\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print('i made your '+sandwich)
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print('\t'+sandwich)