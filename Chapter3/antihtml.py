import urllib
import sys
import re

url=sys.argv[1]
basename=url.split('/')[-1]
if basename=='':
    basename='index.html'
file(basename,'w')
urllib.urlretrieve(url,basename)
f=open(basename,'r')
for line in f:
    match=re.search(r'(<.*>)(.*)',line)
    if match:
        print match.group(2)

