
import operator

def read():
    f = open("euler18.txt")
    cleanlines = [map(int, line.split()) for line in f]
    f.close()
    return cleanlines

def best(line):
    return map(lambda val: max(*val), zip(line, line[1:]))

def merge(a, b):
    return map(sum, zip(a, b))

def solve():
    lines = read()
    abc = None
    for line in reversed(lines):
        if abc:
            line = merge(abc, line)
        if len(line) > 1:
            abc = best(line)
    return line
        
