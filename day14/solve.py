import time
from collections import defaultdict

def parse_cave():
    xmin = float('inf')
    xmax = 0
    ymax = 0
    paths = []
    for line in open('input.txt'):
        path = line.strip().split(' -> ')
        points = []
        for point in path:
            x, y = map(int, point.split(','))
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y
            points.append((x, y))
        paths.append(points)
    cave = []
    for i in range(ymax + 2):
        cave.append(['.'] * (xmax - xmin + 20))
    for path in paths:
        for i, fpoint in enumerate(path[:-1]):
            tpoint = path[i + 1]
            fx, fy = fpoint[0] - xmin + 10, fpoint[1]
            tx, ty = tpoint[0] - xmin + 10, tpoint[1]
            if fx == tx:
                if fy > ty:
                    for j in range(ty, fy + 1):
                        cave[j][fx] = '#'
                else:
                    for j in range(fy, ty + 1):
                        cave[j][fx] = '#'
            else:
                if fx > tx:
                    for j in range(tx, fx + 1):
                        cave[ty][j] = '#'
                else:
                    for j in range(fx, tx + 1):
                        cave[ty][j] = '#'
    return cave, xmin, ymax

def print_cave(cave):
    print('\n'.join(''.join(l) for l in cave))

def task1():
    cave, xmin, ymax = parse_cave()
    start = 500 - xmin + 10, 0
    i, j = start
    t = 0
    sands = 0
    while True:
        if j > ymax:
            break
        if cave[j + 1][i] == '.':
            cave[j][i] = '.'
            j += 1
            cave[j][i] = 'o'
        elif cave[j + 1][i - 1] == '.':
            cave[j][i] = '.'
            j += 1
            i -= 1
            cave[j][i] = 'o'
        elif cave[j + 1][i + 1] == '.':
            cave[j][i] = '.'
            j += 1
            i += 1
            cave[j][i] = 'o'
        else:
            i, j = start
            sands += 1
    return sands


def task2():
    cave, xmin, ymax = parse_cave()
    cave.append(['#'] * len(cave[0]))
    print_cave(cave)
    infinite_cave = defaultdict(lambda: defaultdict(lambda: '.'))
    for i, line in enumerate(cave):
        for j, c in enumerate(line):
            infinite_cave[i][j] = c
    for i in range(-5000, 5000):
        infinite_cave[ymax + 2][i] = '#'
    start = 500 - xmin + 10, 0
    i, j = start
    sands = 0
    while True:
        if infinite_cave[j + 1][i] == '.':
            infinite_cave[j][i] = '.'
            j += 1
            infinite_cave[j][i] = 'o'
        elif infinite_cave[j + 1][i - 1] == '.':
            infinite_cave[j][i] = '.'
            j += 1
            i -= 1
            infinite_cave[j][i] = 'o'
        elif infinite_cave[j + 1][i + 1] == '.':
            infinite_cave[j][i] = '.'
            j += 1
            i += 1
            infinite_cave[j][i] = 'o'
        elif (i, j) == start:
            infinite_cave[j][i] = 'o'
            sands += 1
            break
        else:
            i, j = start
            sands += 1
    return sands


if __name__ == '__main__':
    print(task1())
    print(task2())
