def group(list1,size):
    result=[]
    s=0
    e=size
    i=1
    while i<=len(list1):
        new=[]
        for item in range(s,e):
            if item<len(list1):
                new.append(list1[item])
        result.append(new)
        s+=size
        e+=size
        i+=size
    return result

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
 
