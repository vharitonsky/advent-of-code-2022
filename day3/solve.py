import string

ALL_LETTERS = string.ascii_lowercase + string.ascii_uppercase

PRIORITY = {
    letter: i for letter, i in zip(ALL_LETTERS, range(1, len(ALL_LETTERS) + 1))
}


def task1():
    score = 0
    for line in open('input.txt'):
        line = line.strip()
        line_len = len(line)
        part1, part2 = line[:line_len//2], line[line_len//2:]
        for c in part1:
            if c in part2:
                score += PRIORITY[c]
                break
    return score


def task2():
    score = 0
    groups = [[]]
    i = 0
    k = 0
    for line in open('input.txt'):
        if i == 3:
            i = 0
            k += 1
            groups.append([])
        line = line.strip()
        groups[k].append(line)
        i += 1
    for g in groups:
        for c in g[0]:
            if c in g[1] and c in g[2]:
                score += PRIORITY[c]
                break
    return score


if __name__ == '__main__':
    print(task1())
    print(task2())
