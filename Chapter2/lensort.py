def lensort(list1):
   result=sorted(list1,key=lambda x:len(x))
   return result

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
