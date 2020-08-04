import numpy
from math import *

# raw = raw_input().split()
# a = numpy.array(map(int, raw))

l = numpy.array([3,8,0,1,2,7,4,6,5])
n = int(numpy.sqrt(len(l)))

size = len(l)
part = sqrt(size)
solve = ""

def verif():
    for i in range(len(l)):
        if i not in l:
            exit(84)

def rotateLine(lineNb, dir, rotNb, l):
    print("Rotate line", lineNb, "to ", dir, rotNb, "times")
    a = numpy.reshape(l, (n, n))
    numpy.roll(a[lineNb], rotNb)
    l = a.flatten()

def rotateCol(colNb, dir, rotNb,l):
    print("Rotate col", colNb, "to ", dir, rotNb, "times")
    a = numpy.reshape(l, (n, n))
    a = numpy.transpose(a)
    numpy.roll(a[colNb], rotNb)
    a = numpy.transpose(a)
    l = a.flatten()

for i in range(len(l)):

    if i % part == 0 and floor(float(numpy.where(l == i)[0][0]) / float(part)) == floor(float(i) / float(part)):
        rotateLine(floor(float(i) / float(part)), "W", int(numpy.where(l == i)[0][0] % part), l)
        continue