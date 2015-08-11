def dup(list1):
    new={}
    for i in list1:
        if i in new.keys():
             new[i]+=1
        else:
             new[i]=1
    result=[]
    for i,j in new.items():
        if j>1:
            result.append(i)
    return result



print dup([1,2,1,3,2,5])
    
