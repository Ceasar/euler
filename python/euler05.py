from collections import Counter as multiset
from itertools import chain

from euler3 import prime_factors
import shorthand


def divisors(n):
  """
  >>> [i for i in sorted(divisors(36))]
  [1, 2, 3, 4, 6, 9, 12, 18, 36]
  """
  divides = shorthand.divides
  for i in xrange(1, int(n ** 0.5) + 1):
    if divides(n, i):
      yield i
      if n / i != i:
        yield n / i


def gcd(a, b):
  """
  >>> gcd(48, 180)
  12
  """
  while b != 0:
    a, b = b, a % b
  return a


def lcm(a, b):
  """
  >>> lcm(48, 180)
  720
  """
  return a * b / gcd(a, b)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
