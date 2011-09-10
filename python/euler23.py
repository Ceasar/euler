
import euler

def abundant(n):
    '''Determine if a number is abundant.'''
    return n < sum(proper_divisors(n))

def euler23():
    a = set(range(12, 28124, 2) + range(12, 28124, 3))
    print "got a"
    b = filter(abundant, a)
    print "got b"
    c = all_sums(b)
    print "got c"
    d = set(range(28124)) - c
    print "got d"
    e = sum(d)
    print "got e"
    return e
