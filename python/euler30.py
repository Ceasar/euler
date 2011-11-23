from itertools import product

nums = range(10)
for num in product(*([nums] * 5)):
	print num

