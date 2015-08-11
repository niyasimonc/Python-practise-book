import itertools
import sys

def mutate(word,item):
    word.lower()
    word_list=list(word)
    l=[[i]+word_list for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]
    words=[word]
    w=''
    for i in l:
        for j in i:
            w+=j
        words.append(w)
        w=''
  
    
    
    d=list(itertools.combinations(word,4))
    w=''
    l=[]
    for i in d: 
        for j in i:
          w+=j
        l.append(w)
        w=''
    l=list(set(l))   
    for i in l:
      words.append(i)
 
    
    new=[i+j for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] for j in l]
    w=''
    l=[]
    for i in new:
        for j in i:
            w+=j
        l.append(w)
        w=''    
    l=list(set(l))
    for i in l:
       words.append(i)
  

    if item in words:
         return True
 
    items=list(item)
    c=0
    for i in words:
        if len(items)==len(i):
            li=list(i)
            for j in items:
               if j in li:
                   c+=1
        
        if c==len(item):
             return True
        else: 
             return False

    

print mutate(sys.argv[1],sys.argv[2])
