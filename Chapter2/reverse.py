def reverse(list1):
    result=[list1[-i] for i in range(1,len(list1)+1)]
    return result

print reverse(reverse([1,2,3,4]))
    
