import operator

from memoizer import *

def all_sums(nums):
    '''Get all possible sums via adding any two numbers in nums.'''
    sums = set([])
    nums = nums[:]
    while nums:
        a = nums.pop()
        sums.add(2 * a)
        map(sums.add, map(a.__add__, nums))
    return sums

def iter_triangle_numbers():
    '''Iterate over the triangle numbers.'''
    i = 0
    while 1:
        i += 1
        yield i * (i + 1) / 2

def pythagorean_triple(m, n):
    '''Generate a pythagorean triple.'''
    return m * m - n * n, 2 * m * n, m ** 2 + n ** 2

def proper_divisors(n):
    '''Get the proper divisors of n.'''
    return set(factor(n)[1:])

def factor(n):
    '''Get the integer factorization of n.'''
    sieve = xrange(1, n ** 0.5 + 1)
    return sum([[ n / x, x] for x in sieve if not n % x], [])

def gcd(*args):
    '''Get the greatest common divisor.'''
    factored = {}
    for arg in args:
        factored[arg] = prime_factors(arg)
    common = set(sum(factored.values()), [])
    def least(num):
        return num ** min([factored[arg].count(num) for arg in args])
    return reduce(operator.mul, [least(num) for num in common])

def lcm(*args):
    '''Get the least common multiple.'''
    factored = {}
    for arg in args:
        factored[arg] = prime_factors(arg)
    common = set(sum(factored.values()), [])
    def most(num):
        return num ** max([factored[arg].count(num) for arg in args])
    return reduce(operator.mul, [most(num) for num in common])

def prime_factors(n):
    '''Get the prime factors of n.'''
    if n < 2:
        return []
    factors = []
    xprimes = primes(n ** 0.5)
    while n > 1:
        try:
            prime = xprimes.pop(0)
            while prime:
                if n % prime == 0:
                    xprimes.insert(0, prime)
                    factors.append(prime)
                    n /= prime
                    break
                prime = xprimes.pop(0)
        except:
            return factors + [n]
    return factors

def primes(n):
    '''Get all primes up to and including n.'''
    n = int(n)
    if n < 2:
        return []
    elif n == 2:
        return [2]
    sieve = range(3, n + 1, 2)
    mid = (n + 1) / 2 - 1
    index = 0
    jump = 3
    root = n ** 0.5
    while jump <= root:
        if sieve[index]:
            j = (jump ** 2 - 3) / 2
            while j < mid:
                try:
                    sieve[j] = 0
                except:
                    print j, len(sieve), mid
                    raise
                j += jump
        index += 1
        jump += 2
    return [2] + [x for x in sieve if x]
