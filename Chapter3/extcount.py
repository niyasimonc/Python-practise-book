import sys
import os
import re



def exc(dire):
    list1=os.listdir(dire)
    new={}
    for item in list1:
        match=re.search(r'(\w+)(.)(\w+)',item)
        if match:
          if new.get(match.group(3))==None:
              new[match.group(3)]=[item]
          else:
              new[match.group(3)].append(item)
    for keys in new.keys():
       print     keys,':  ',len(new[keys])


exc(sys.argv[1])
