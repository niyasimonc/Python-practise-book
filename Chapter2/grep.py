import re
import sys

def grep(file_name,pattern):
    f=open(file_name,'r')
    result=[]
    for line in f:
        match=re.search(pattern,line)
        if match:
            result.append(line)
    for i in result:
        print i
    return



grep(str(sys.argv[1]),str(sys.argv[2]))

