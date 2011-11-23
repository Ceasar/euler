from itertools import combination

i = 0
while 9 ** i < a * i:
  i += 1
#i is the max length of the number

for combination in combinations(range(9), i):
  if sum(
