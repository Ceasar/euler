

def fib():
  i, j = 0, 1
  while True:
    yield i
    i, j = j, i + j


if __name__ == '__main__':
  import itertools
  print sum(x for x in itertools.takewhile(lambda x: x <= 4000000, fib()) if x % 2 == 0)
