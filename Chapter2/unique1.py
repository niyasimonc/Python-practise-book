def unique(list1,key):
    new=list(set(list1))
    result=[]
    for i in new:
       result.append(key(i))
    return list(set(result))

print unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
