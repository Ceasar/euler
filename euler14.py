import memoizer

@memoizer.Memoizer
def foo(n):
    try:
        if n == 1:
            return 1
        if n % 2:
            return foo(3 * n + 1) + 1
        else:
            return foo(n / 2) + 1
    except ValueError as e:
        raise e
    except:
        raise ValueError(n)

def bar(n):
    if n == 1:
        return 1
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2

'''Basically just a hack. Everytime recursion depth is exceeded, it gets the
number it left off at and adds it to crazies to start there next time, thus
guaranteeting a solution.'''
def euler14():
    big = 0
    best = None
    crazies = []
    for num in range(1, 1000001):
        try:
            new = foo(num)
            if new > big:
                print "big", new
                big = new
                best = num
        except ValueError as e:
            print e.args[0], num
            crazies.append(e.args[0])
            crazies.append(num)
    while len(crazies):
        num = crazies.pop(0)
        try:
            new = foo(num)
            if new > big:
                print "big", new
                big = new
                best = num
        except ValueError as e:
            print e.args[0], num
            crazies.append(e.args[0])
            crazies.append(num)
    return best
