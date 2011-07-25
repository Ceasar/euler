
a = 2 ** 1000
b = str(a)
print reduce(lambda x, y: int(x) + int(y), b)
