from itertools import izip as zip


def read_nums():
    """Parse all the numbers on each line of a file."""
    with open("euler67.txt") as f:
        for line in f:
            yield [int(i) for i in line.split()]


def select(line):
    for i, j in zip(line, line[1:]):
        yield max(i, j)


def solve(lines):
    rv = [0] * 101
    for line in reversed(lines):
        rv = [i + j for i, j in zip(select(rv), line)]
    return rv

if __name__ == "__main__":
    print solve(list(read_nums()))[0]
