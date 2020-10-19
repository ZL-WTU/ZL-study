def build_profile(first,last,**user_info):
    profile={}
    profile['first']=first
    profile['last']=last
    for k,v in user_info.items():
        profile[k]=v
    return profile
user_info=build_profile("albert",'einstein',loction='princeton',field='math')
print(user_info)