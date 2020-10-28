def fun(city_name,country_name,pupulation_num=''):
    A=city_name.title()
    B=country_name.title()
    if pupulation_num:
        C=A+','+B+'-'+'population'+' '+str(pupulation_num)
    else:
        C=A+' '+B
    return C