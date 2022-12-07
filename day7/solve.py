class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.name_map = {}

    def add_dir(self, name):
        d = Dir(name)
        self.dirs.append(d)
        self.name_map[name] = d
        return d

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def get_dir(self, name):
        return self.name_map[name]

    def size(self):
        return (
            sum(f.size for f in self.files) + sum(d.size() for d in self.dirs)
        )


def parse_dirs():
    root = Dir('/')
    dirs = [root]
    all_dirs = [root]
    f = open('input.txt')
    next(f)
    for line in f:
        line = line.strip()
        if line.startswith('$ cd'):
            if line.endswith('..'):
                dirs.pop()
            else:
                parent = dirs[-1]
                dirname = line[5:]
                d = parent.get_dir(dirname)
                all_dirs.append(d)
                dirs.append(d)
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            dirname = line.split()[-1]
            parent = dirs[-1]
            parent.add_dir(dirname)
        elif line[0].isdigit():
            size, name = line.split()
            parent = dirs[-1]
            parent.add_file(name, int(size))
    return all_dirs


def task1():
    all_dirs = parse_dirs()
    sizes = [d.size() for d in all_dirs]
    return sum(s for s in sizes if s <= 100000)


def task2():
    all_dirs = parse_dirs()
    unused = 70000000 - all_dirs[0].size()
    needed = 30000000 - unused
    dirs = [d for d in all_dirs if d.size() >= needed]
    return sorted(dirs, key=lambda d: d.size(), reverse=True)[-1].size()


if __name__ == '__main__':
    print(task1())
    print(task2())
