import operator

import euler

def d(n):
    return sum(proper_divisors(n))

def amicable(cutoff):
    amicables = set([])
    sieve = set(range(2, cutoff)) - set(primes(cutoff))
    while sieve:
        a = sieve.pop()
        b = d(a)
        while 1:
            #print a, b
            if b in sieve:
                sieve.remove(b)
                c = d(b)
                if c == a:
                    amicables.add(a)
                    amicables.add(b)
                    break
                else:
                    a = b
                    b = c
            else:
                break
    return amicables

def euler21():
    return sum(map(d, range(1, 1000)))
