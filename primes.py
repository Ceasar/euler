import bisect, math

from sortedlist import SortedList

class PrimeList(SortedList):
    '''A manager for functions dealing with primes.'''
    def __init__(self, n):
        super(PrimeList, self).__init__(primes(n))

    def extend(self, n):
        '''Extend the list of primes up to n.'''
        self += [prime for prime in xprimes(n, self)]

    def is_prime(self, n):
        '''Quickly checks if a number is prime.'''
        if n > self[-1]:
            self.extend(3 * n / 2)
        return n == self[bisect.bisect_left(self, n)]

def is_prime(n):
    '''Check if a number is prime.'''
    sieve = primes(n ** 0.5)
    i = 0
    try:
        while n % sieve[i]:
            i += 1
        return False
    except:
        return True
    

def xprimes(stop=None, found=None):
    '''Generate primes up to stop using a list of already found primes.'''
    if found is None:
        found = [2]
        yield 2
    else:
        found = found[:]
        offset = found[-1]
    offset = found[-1]
    index = offset
    root = 1
    sieve = range(index, index ** 2 + 1)
    if found == [2]:
        sieve[0] = 0
    if stop is None:
        stop = float("inf")
    else:
        stop = stop - offset
    while stop:
        sqrt = int(math.sqrt(index))
        if sqrt != root:
            root = sqrt
            start = root ** 2 + 1
            end = (root + 1) ** 2 + 1
            sieve.extend(range(start, end))
            i = 0
            while i < len(found):
                curr = found[i]
                j = start / curr * curr - offset
                while j < len(sieve):
                    if j > 0:
                        sieve[j] = 0
                    j += curr
                i += 1
        
        num = sieve[index - offset]
        if num:
            found.append(num)
            sieve = sieve[index - offset:]
            offset = num
            yield num
        
        index += 1
        stop -= 1

def primes(n):
    '''Get all primes up to n.'''
    n = int(n)
    if n < 2:
        return []
    sieve = range(n)
    sieve[1] = 0
    root = n ** 0.5
    index = 0
    while index <= root:
        if sieve[index]:
            i = index ** 2
            while i < n:
                sieve[i] = 0
                i += index
        index += 1
    return [x for x in sieve if x]

##def primes2(n):
##    '''Get all primes up to and including n.'''
##    n = int(n)
##    if n < 2:
##        return []
##    elif n == 2:
##        return [2]
##    small = 3
##    offset = 2
##    sieve = range(3, n + 1, offset)
##    mid = (n + 1) / 2 - 1
##    index = 0
##    jump = small
##    root = n ** 0.5
##    while jump <= root:
##        if sieve[index]:
##            j = (jump ** 2 - small) / offset
##            while j < mid:
##                sieve[j] = 0
##                j += jump
##        index += 1
##        jump += offset
##    return [2] + [x for x in sieve if x]
