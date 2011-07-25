from numpy import array

from memoizer import *

def read_matrix(filename):
    f = open(filename)
    cleaned = map(int, f.readlines())
    f.close()
    return cleaned

def solve(y):
    matrix = read_matrix("euler12.txt")
    p = y ** -1
    return sum(map(lambda x: x ** p, matrix)) ** y

    

##def euler12():
##    for num in iter_triangle_numbers():
##        if len(factor(num)) > 500:
##            print num
##            break
    
