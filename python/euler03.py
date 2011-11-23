

divides = lambda x, y: x % y == 0

def prime_factors(n):
  i = 2
  while i < n ** 0.5:
    if divides(n, i):
      yield i
      n /= i
      i = 2
    else:
      i += 1
  yield n

if __name__ == '__main__':
  print max(prime_factors(600851475143))
