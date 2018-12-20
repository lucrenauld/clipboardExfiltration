import sys

print sys.argv[1]
f = open('clip.log', 'w')
f.write(sys.argv[1])
f.close()
