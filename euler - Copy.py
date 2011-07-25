import operator
import bisect

from memoizer import Logger
from primes import *

def inc():
    n = 0
    yield 0
    while 1:
        n += 1
        if n == 1000:
            break
        yield n
        yield -n

primelist = primes(16000)
def consecutive_primes(a, b):
    n = 0
    y = n ** 2 + a * n + b
    #print "a", a, "b", b, "y", y
    while is_prime(y, primelist):
        n += 1
        y = n ** 2 + a * n + b
    #print "-------------------"
    #print "a", a, "b", b, "N", n
    return n

def foo(a):
    ns = map(lambda b: consecutive_primes(a, b), primelist)
    n = max(ns)
    print "a", a, n, "prime", primelist[ns.index(n)]
    return n
    

def curve():
    best = map(foo, inc())
    return max(best)
        

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
    return set(factors(n)[1:])

def factors(n):
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

def make_odd(n):
    '''Make n odd.'''
    return (n + 1) / 2 * 2 - 1

def remove_multiples(a, b):
    '''Remove all multiple of numbers in a from b via turning them into 0s.'''
    first = b[0]
    len_sieve = max(b)
    sieve = range(len_sieve + 1)
    
    a_i = 0
    len_a = len(a)
    while a_i < len_a:
        curr_a = a[a_i]
        if curr_a:
            sieve_i = curr_a
            while sieve_i < len_sieve:
                sieve[sieve_i] = 0
                sieve_i += curr_a
        a_i += 1
    return [sieve[x] for x in b]


