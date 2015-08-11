import sys

def wordwrap(filename,width):
    f=open(filename,'r')
    for line in f:
       if len(line)>width:
           if line[width]==' ':
               print line[:width]
               print line[width:]
           else:
              while(line[width]!=' '):
                   width-=1
              print line[:width]
              print line[width+1:]
    return



wordwrap(str(sys.argv[1]),int(sys.argv[2]))



