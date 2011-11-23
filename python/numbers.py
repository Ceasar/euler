from __future__ import division


# Used in Euler 010
# Used in Euler 007
def primes(n):
    '''Get all primes up to n.
    >>> primes(10)
    set([2, 3, 5, 7])'''
    assert type(n) == int
    if n < 2:
      return set()
    else:
      sieve = range(n)
      sieve[1] = 0 
      for index in range(int(n ** 0.5) + 1): 
        if sieve[index]:
          i = index ** 2
          while i < n:
            sieve[i] = 0 
            i += index
      return set(i for i in sieve if i)


#Used in Euler 002
def fibonacci():
  """Generate the fibonacci numbers.
  The fibonacci numbers are defined as:
  * fib(n) = fib(n-1) + fib(n-1)
  * fib(0) = 0, fib(1) = 1
  """
  i, j = 0, 1
  while True:
    yield i
    i, j = j, i + j


# Used in Euler 003
def prime_factors(n):
  """Generate the prime factors on n.
  >>> [i for i in prime_factors(9)]
  [3, 3]
  >>> [i for i in prime_factors(10)]
  [2, 5]
  >>> [i for i in prime_factors(288)]
  [2, 2, 2, 2, 2, 3, 3]
  """
  for prime in primes(int(n ** 0.5) + 1):
    if n % prime == 0:
      return [prime] + prime_factors(n // prime)
  return [n]


def divisors(n):
  """Get the divisors of n.
  >>> [i for i in sorted(divisors(36))]
  [1, 2, 3, 4, 6, 9, 12, 18, 36]
  """
  for i in xrange(1, int(n ** 0.5) + 1): 
    if n % i == 0:
      yield i
      if n // i != i:
        yield n // i 


# Used in Euler 004
def palindrome(x):
  """Check if x is a palindrome.
  >>> palindrome('racecar')
  True
  >>> palindrome('euler')
  False
  """
  y = str(x)
  return y == y[::-1]


def gcd(a, b): 
  """Get the greatest common divisor of a and b.
  >>> gcd(48, 180)
  12
  """
  while b != 0:
    a, b = b, a % b 
  return a


# Used in Euler 005
def lcm(a, b): 
  """Get the least common multiple of a and b. 
  >>> lcm(48, 180)
  720
  """
  return a * b // gcd(a, b)


# Used in Euler 009
def pythagorean_triple(m, n):
    '''Generate a pythagorean triple.
    >>> pythagorean_triple(2, 1)
    (3, 4, 5)
    '''
    assert m > n
    return m * m - n * n, 2 * m * n, m ** 2 + n ** 2


# Used in Euler 012
def triangle_numbers():
    '''Generate the triangle numbers.'''
    i = 0
    while True:
      i += 1
      yield i * (i + 1) / 2


def proper_divisors(n):
    '''Get the proper divisors of n.'''
    return set(factor(n)[1:])


def amicables():
  def d(n):
    return sum(proper_divisors(n))
  a = 1
  while True:
    b = d(a)
    if d(b) == a and a != b:
      yield a
    a += 1


def all_sums(nums):
    '''Get all possible sums via adding any two numbers in nums.'''
    sums = set([])
    nums = nums[:]
    while nums:
        a = nums.pop()
        sums.add(2 * a)
        map(sums.add, map(a.__add__, nums))
    return sums


def cycle(n):
  remainders = set()
  remainder = 10
  while True:
    remainder /= n * 10
    if remainder in remainders:
      print remainders
      return len(remainders)
    else:
      remainders.add(remainder)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
