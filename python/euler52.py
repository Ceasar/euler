
def euler52():
  n = 1
  i  = 0
  js = range(2, 7)
  while True:
    i = 10 ** n
    k = 10 * i / 6.0
    while i < k:
      expected = set(str(i))
      for j in js:
        if set(str(i * j)) != expected:
          break
      i += 1
    n += 1

print euler52()
