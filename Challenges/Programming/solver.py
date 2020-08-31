import numpy
from math import *

# raw = raw_input().split()
# a = numpy.array(map(int, raw))

l = numpy.arange(100* 100)
numpy.random.shuffle(l)

n = int(numpy.sqrt(len(l)))

size = len(l)
part = sqrt(size)
solve = ""

def printTab():
    for i in range (int(part)):
        for j in range(int(part)):
            print(l[int(i * part) + j],"", end="")
        print("")
    print("")

def sline(i):
    return floor(i / part)

def line(i):
    return floor(numpy.where(l == i)[0][0] / part)

def cline(i):
    return line(i) == sline(i)

def scol(i):
    return int(i % part)

def col(i):
    return int(numpy.where(l == i)[0][0] % part)

def ccol(i):
    return scol(i) == col(i)

def verif():
    if (len(numpy.unique(l)) != len(l)):
        exit(84)
    for i in range(len(l)):
        if i not in l:
            exit(84)

def rotateLine(lineNb, dir, rotNb):
    #print("Rotate line", lineNb, "to ", dir, rotNb, "times")
    global solve, l
    solve += str(lineNb)
    solve += dir
    solve += str(rotNb)
    solve += ","
    a = numpy.reshape(l, (n, n))
    a[lineNb] = numpy.roll(a[lineNb], rotNb if dir == "E" else -rotNb)
    l = a.flatten()

def rotateCol(colNb, dir, rotNb):
    #print("Rotate col", colNb, "to ", dir, rotNb, "times")
    global solve, l
    solve += str(colNb)
    solve += dir
    solve += str(rotNb)
    solve += ","
    a = numpy.reshape(l, (n, n))
    a = numpy.transpose(a)
    a[colNb] = numpy.roll(a[colNb], rotNb if dir == "S" else -rotNb)
    a = numpy.transpose(a)
    l = a.flatten()

import time
start_time = time.time()

#printTab()
for i in range(len(l) - int(part) + 1):
    #print(i)
    if cline(i) and ccol(i):
        #print("Do nothing with", i)
        continue
    if scol(i) == 0 and cline(i):
        rotateLine(line(i), "W", col(i))
        #printTab()
        continue
    if sline(i) == 0 and cline(i) and col(i) != scol(i):
        rotateCol(col(i), "S", 1)
        rotateLine(1, "E" if scol(i) > col(i) else "W", abs(scol(i) - col(i)))
        rotateCol(col(i), "N", 1)
        #printTab()
        continue
    if cline(i) and not ccol(i):
        rotateCol(col(i), "N", 1)
        rotateLine(sline(i), "E" if scol(i) < col(i) else "W", abs(scol(i) - col(i)))
        rotateCol(col(i), "S", 1)
        rotateLine(line(i), "E" if scol(i) > col(i) else "W", abs(scol(i) - col(i)))
        #printTab()
        continue
    if ccol(i) and not cline(i):
        rotateLine(line(i), "E", 1)
    if not ccol(i) and not cline(i):
        rotateCol(scol(i), "N" if sline(i) > line(i) else "S", abs(sline(i) - line(i)))
        rotateLine(line(i), "E" if scol(i) > col(i) else "W", abs(scol(i) - col(i)))
        rotateCol(scol(i), "N" if sline(i) < line(i) else "S", abs(sline(i) - line(i)))
        #printTab()
        continue
for i in range (len(l) - int(part) + 1, len(l) -2):
    #print(i)
    while not ccol(i):
        pos = col(i)
        if (col(i) == int(part) - 1):
            rotateCol(int(part) -2, "S", 1)
            rotateLine(int(part - 1), "E", 1)
            rotateCol(int(part) -2, "N", 1)
            rotateLine(int(part - 1), "W", 2)
            rotateCol(int(part) -2, "S", 1)
            rotateLine(int(part - 1), "E", 1)
            rotateCol(int(part) -2, "N", 1)
        else:
            rotateCol(pos, "S", 1)
            rotateLine(int(part - 1), "E", 1)
            rotateCol(pos, "N", 1)
            rotateLine(int(part - 1), "W", 2)
            rotateCol(pos, "S", 1)
            rotateLine(int(part - 1), "E", 1)
            rotateCol(pos, "N", 1)
        #printTab()
    #printTab()
if not numpy.all(l[:-1] <= l[1:]):
    for i in range(int(part) - 1):
        rotateCol(int(part - 2), "N", 1)
        rotateLine(int(part - 1), "W", 1)
        rotateCol(int(part - 2), "S", 1)
        rotateLine(int(part - 1), "E", 1)
        rotateCol(int(part - 2), "N", 1)
#printTab()
solve = solve[:-1]
#print(solve)
if numpy.all(l[:-1] <= l[1:]):
    print("EASY MGL")
    print("--- %s seconds ---" % (time.time() - start_time))