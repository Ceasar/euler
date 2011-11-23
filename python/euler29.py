from itertools import product

results = set()
a = range(2, 101)
b = range(2, 101)
for i, j in product(a, b):
  results.add(i ** j)
print len(results)
