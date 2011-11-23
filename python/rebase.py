


def rebase(i, b):
  new = []
  while i > 0:
    new.append(str(i % b))
    i = i / b
  return "".join(reversed(new))

print rebase(9474, 4)
print rebase(8208, 4)
print rebase(1634, 4)
