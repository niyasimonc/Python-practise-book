def cumulative(list1):
    result=[]
    result.append(list1[0])
    i=1
    while(i<len(list1)):
         result.append(list1[i-1]+list1[i])
         i+=1
    return result


print cumulative(['di','ds','gt','dd'])
