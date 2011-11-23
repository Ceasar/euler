

def spiral(n):
  """Generate the spiral numbers.
  >>> [i for i in spiral(1)]
  [1]
  >>> [i for i in spiral(3)]
  [1, 3, 5, 7, 9]
  >>> [i for i in spiral(5)]
  [1, 3, 5, 7, 9, 13, 17, 21, 25]
  """
  assert n > 0
  assert n % 2
  if n == 1:
    yield n
  else:
    for i in spiral(n - 2):
      yield i
    i = (n - 1)
    j = n * n - 3 * n + 3
    for k in range(4):
      yield j + i * k


if __name__ == '__main__':
  import doctest
  doctest.testmod()
