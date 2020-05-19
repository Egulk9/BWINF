import sys

x = 0
for line in sys.stdin:
    print(type(line))
    print(x)
    x+=1
