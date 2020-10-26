reason='reason.txt'
while True:
    rea=input('Whats the reason that you like programming?,end with quit:')
    if rea=='quit':
        break
    else:
        with open(reason,'a') as REA:
            REA.write(rea+'\n')

