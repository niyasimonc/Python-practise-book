import zipfile
import sys

print 'creating archive'
zf = zipfile.ZipFile(sys.argv[1], mode='w')
print 'adding files'
for files in sys.argv[2:]:
  zf.write(files)
print 'closing'
zf.close()

