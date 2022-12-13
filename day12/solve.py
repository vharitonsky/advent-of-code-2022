class HeightMap:

    def __init__(self, topo):
        self.topo = topo

    def get_low(self):
        for i, line in enumerate(self.topo):
            for j, c in enumerate(line):
                if c == 97:
                    yield i, j

    def get_height(self, i, j):
        return self.topo[i][j]

    def get_paths(self, i, j):
        height = self.get_height(i, j)
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if i + di < 0 or i + di == len(self.topo):
                continue
            if j + dj < 0 or j + dj == len(self.topo[0]):
                continue
            if self.get_height(i + di, j + dj) > height + 1:
                continue
            yield i + di, j + dj


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


def traverse(height_map, node):
    queue = [node]
    visited = {node,}
    paths = {}

    while queue:
        new_path = queue.pop(0)
        for path in height_map.get_paths(*new_path):
            if path not in visited:
                visited.add(path)
                queue.append(path)
                paths[path] = new_path
    return paths


def task1():
    topo, start, end = parse_map()
    height_map = HeightMap(topo)
    paths = traverse(height_map, start)
    node = end
    shortest = []
    while True:
        shortest.append(node)
        if paths[node] == start:
            break
        node = paths[node]
    return len(shortest)


def task2():
    topo, _, end = parse_map()
    height_map = HeightMap(topo)
    min_steps = float('inf')
    for start in height_map.get_low():
        node = end
        paths = traverse(height_map, start)
        shortest = []
        while True:
            shortest.append(node)
            if node not in paths:
                break
            if paths[node] == start:
                if len(shortest) < min_steps:
                    min_steps = len(shortest)
                break
            node = paths[node]
    return min_steps


if __name__ == '__main__':
    print(task1())
    print(task2())
