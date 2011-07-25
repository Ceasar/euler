
import operator

def char2word(char):
    mydict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }
    return mydict[char]

def n(num):
    a = num / 100
    b = num % 100 / 10 * 10
    c = num % 10
    output = ""
    if a > 0:
        output += char2word(a) + "hundred"
        if b > 0 or c > 0:
            output += "and"
    d = num % 100
    if 0 < d < 20:
        output += char2word(d)
        return len(output) 
    if b > 0:
        output += char2word(b)
    if c > 0:
        output += char2word(c)
    return len(output)

def euler17():
    a = reduce(operator.add, map(n, range(1, 1000)))
    a += len("onethousand")
    return a
    
