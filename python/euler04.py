
palindrome = lambda x: x == x[::-1]

if __name__ == '__main__':
  from itertools import product
  print max(x * y for x, y in product(xrange(100, 999), xrange(100, 999)) if palindrome(str(x * y)))
