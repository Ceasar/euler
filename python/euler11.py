
import time

from numpy import array

from memoizer import *

def m1(x):
    return [x[i] * x[i + 1] for i in xrange(len(x) - 1)]

def m2(array):
    return [array[i] * array[i + 2] for i in xrange(len(array) - 2)]

def read_matrix(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    cleaned = [map(int, line.split()) for line in lines]
    return array(cleaned)

def flip(x):
    y = list(x)[:]
    y.reverse()
    return y

def get():
    matrix = read_matrix("euler11.txt")
    transpose = matrix.transpose()
    reverse = array([flip(line) for line in matrix])
    reverse_transpose = reverse.transpose()

    print "matrix"
    for line in matrix:
        yield line
    print "transpose"
    for line in transpose:
        yield line
    print "diagonals"
    width = len(line)
    for i in range(width):
        yield matrix[i:].diagonal()
        yield transpose[i:].diagonal()
        yield reverse[i:].diagonal()
        yield reverse_transpose[i:].diagonal()

biggest = [max(m2(m1(x))) for x in get() if len(x) > 3]
    
    
    
    

#sums = [sum(array) for array in nums()]
#paired = [(x, y) for x, y in zip(sums, biggest)]

    

    
