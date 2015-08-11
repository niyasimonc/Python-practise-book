def reverse(filename):
    f=open(filename,'r')
    content=[]
    for line in f:
        content.append(line)
    for i in range(1,len(content)+1):
        print content[-i]


reverse("she.txt")
