import product

def factorial(n):
    result=[]
    if n==0:
       return 1
    else:
       for idx in range(1,n+1):
           result.append(idx)
    return product.product(result)


print factorial(5)    
       

    
