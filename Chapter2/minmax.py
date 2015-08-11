def mini(list1):
    minimum=[]
    if len(minimum)==0:
       minimum.append(list1[0])
    for item in list1:            
        mini=minimum.pop()
        if item<mini:
            minimum.append(item)
        else:
            minimum.append(mini)
    return minimum.pop()


def maxi(list1):
    maximum=[]
    if len(maximum)==0:
        maximum.append(list1[0])
    for item in list1:
        maxi=maximum.pop()
        if item>maxi:
           maximum.append(item)
        else:
           maximum.append(maxi)
    return maximum.pop()



