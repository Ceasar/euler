"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
"""
from collections import defaultdict


TRIANGLES = defaultdict(list)


def upto(n):
    """Get all the numbers up to and including n."""
    for i in range(n + 1):
        yield i


def gen_doubles(m, n):
    for i in upto(m):
        for k in upto(n):
            yield i, k


def gen_right_triangles(n):
    """Generate all right triangles with max side length `n`."""
    # huge mess. found this online. need to prove this actually works.
    # empirically, seems to work though
    for a, j in gen_doubles(n, n):
        if 0 in (a, j):
            continue
        if (a * a) % j != 0:
            continue
        if a / j < 2:
            continue
        k = ((a ** 2) / j - 2 * a - j)
        if k % 2 != 0:
            continue
        i = k / 2
        if i <= 0:
            continue
        b, c = a + i, a + i + j
        yield a, a + i, a + i + j


def main():
    for a, b, c in gen_right_triangles(1000):
        TRIANGLES[a + b + c].append((a, b, c))
    k = max(TRIANGLES, key=lambda k: len(TRIANGLES[k]) if k < 1000 else 0)
    print k

if __name__ == "__main__":
    main()
