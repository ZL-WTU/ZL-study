def make_album(singer_name,album_name,sings_number=''):
    message={'singer_name':singer_name,'album_name':album_name}
    if sings_number:
        message['sings_name']=sings_number
    return  message
while True:
    singer=input("input singer:")
    if singer=='q':
        break
    album=input("input album:")
    mes=make_album(singer,album)
    print(mes)