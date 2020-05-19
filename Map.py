import sys

x = 0
print(sys.argv[1])
for line in sys.argv:
    print(line)


class Streets:

    def __init__(self, start_end_point,length):

        self.point = start_end_point
        self.length = length
