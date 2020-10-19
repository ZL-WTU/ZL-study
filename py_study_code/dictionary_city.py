cities={'wuhan':{'country':'china','population':'100K','fact':'hero'},
        'tokyo':{'country':'japan','population':'50k','fact':'attact'},
        }
for k,v in cities.items():
    print(k.title()+':')
    country=v['country']
    population=v['population']
    fact=v['fact']
    print('\t'+country+'\t'+population+'\t'+'\t'+fact)
