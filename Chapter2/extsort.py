import re
def extsort(list1):
    new={}
    for item in list1:
        match=re.search(r'(\w+)(.)(\w+)',item)
        if match:
          if new.get(match.group(3))==None:
              new[match.group(3)]=[item]
          else:
              new[match.group(3)].append(item)
    new_=sorted(new)
    result=[]
    for item in new_:
        l=new[item]
        for i in range(len(l)):
            result.append(l[i])

    
    return result



print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])   
