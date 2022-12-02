SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

BEATS = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

BEATS_LEFT = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

BEATS_RIGHT = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

DRAW = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}


def task1():
    score = 0
    for line in open('input.txt'):
        left, right = line.strip().split()
        if BEATS[left] == right:
            score += SCORES[right] + 6
        elif DRAW[left] == right:
            score += SCORES[right] + 3
        else:
            score += SCORES[right]
    return score


def task2():
    score = 0
    for line in open('input.txt'):
        left, right = line.strip().split()
        if right == 'X':
            score += SCORES[BEATS_LEFT[left]]
        elif right == 'Y':
            score += SCORES[left] + 3
        else:
            score += SCORES[BEATS_RIGHT[left]] + 6
    return score


if __name__ == '__main__':
    print(task1())
    print(task2())
