def parse_map():
    topo = []
    start = None
    end = None
    for i, line in enumerate(open('input.txt')):
        topo.append([])
        line = line.strip()
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                topo[i].append(ord('a'))
            elif c == 'E':
                end = (i, j)
                topo[i].append(ord('z'))
            else:
                topo[i].append(ord(c))
    return topo, start, end


def traverse(topo, current, end, visited, paths):
    print(len(visited))
    if current == end:
        paths.append(visited)
        return
    ci, cj = current
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (ci + i, cj + j) in visited:
            continue
        if ci + i < 0 or ci + i == len(topo):
            continue
        if cj + j < 0 or cj + j == len(topo[0]):
            continue
        if topo[ci + i][cj + j] > topo[ci][cj] + 1:
            continue
        traverse(topo, (ci + i, cj + j), end, visited | {current, }, paths)


def task1():
    topo, start, end = parse_map()
    paths = []
    traverse(topo, start, end, set(), paths)
    shortest = sorted(paths, key=lambda p: len(p))[0]
    return len(shortest)


def task2():
    pass


if __name__ == '__main__':
    print(task1())
    print(task2())
