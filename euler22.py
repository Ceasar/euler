
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def namescore(line):
    myline = line.lower()
    return sum([alphabet.index(letter) + 1 for letter in myline])

def score(line, index):
    return namescore(line) * (index + 1)

def read():
    f = open("euler22.txt")
    line = f.readline()
    f.close()
    split = line.split(",")
    def clean(name):
        return name[1:-1]
    names = map(clean, split)
    
    names.sort()
    euler_score = sum([score(name, index) for index, name in enumerate(names)])
    return euler_score
    
