import re

dominos_str = input('Enter your dominos (eg. 1 4, 12 6):\n    ')

if not re.compile(r'^\d\d? \d\d?(\s*,\s*\d\d? \d\d?)*$').match(dominos_str):
    print('Invalid dominos input!')
    exit(-1)

double_str  = input('Enter your double (eg. 8):\n     ')

if not re.compile(r'^\d\d?$').match(double_str):
    print('Invalid double input!')
    exit(-1)

dominos = list(map(
    lambda d : list(map(int, d.strip().split(' '))),
    dominos_str.split(',')
))
double  = int(double_str)

def other(domino, side):
    return domino[1] if domino[0] == side else domino[0]

def domino_score(domino):
    return domino[0] + domino[1]

def domino_double(domino):
    return domino[0] == domino[1]

def get_best_sequence(dominos, match):
    choices = []
    for (i, domino) in enumerate(dominos):
        if domino[0] == match or domino[1] == match:
            new_dominos  = dominos[:i] + dominos[i + 1:]
            new_match    = other(domino, match)
            (seq, score) = get_best_sequence(new_dominos, new_match)
            if score != 0 or not domino_double(domino):
                choices.append(([domino] + seq, score + domino_score(domino)))
    best_score = 0
    best_seq = []
    for (seq, score) in choices:
        if score > best_score:
            (best_score, best_seq) = (score, seq)
    return (best_seq, best_score)

def dominos_to_str(dominos, match):
    domino_strs = []
    for domino in dominos:
        domino_strs.append('[' + str(match) + '|' + str(other(domino, match)) + ']')
        match = other(domino, match)
    return ' '.join(domino_strs)

(seq, score) = get_best_sequence(dominos, double)
print(
    'Best sequence:', dominos_to_str(seq, double), 
    '\nWith a score of:', score,
)