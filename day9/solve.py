from collections import defaultdict


def head_around_tail(x, y, tx, ty):
    return (tx, ty) in {
        (x + 1, y),
        (x - 1, y),
        (x, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    }


def sync_tail(x, y, tx, ty):
    if head_around_tail(x, y, tx, ty):
        return tx, ty
    if x > tx:
        tx += 1
    elif x < tx:
        tx -= 1
    if y > ty:
        ty += 1
    elif y < ty:
        ty -= 1
    return tx, ty


def move_head(d, x, y):
    if d == 'R':
        return x + 1, y
    elif d == 'L':
        return x - 1, y
    elif d == 'U':
        return x, y + 1
    elif d == 'D':
        return x, y - 1


def task1():
    grid = defaultdict(lambda: False)
    x, y = 0, 0
    tx, ty = 0, 0
    grid[(x, y)] = True
    for line in open('input.txt'):
        d, s = line.strip().split()
        for i in range(int(s)):
            x, y = move_head(d, x, y)
            tx, ty = sync_tail(x, y, tx, ty)
            grid[(tx, ty)] = True
    return len(grid)


def task2():
    n = 10
    grid = defaultdict(lambda: False)
    knots = defaultdict(lambda: (0, 0))
    grid[(0, 0)] = True
    for line in open('input.txt'):
        d, s = line.strip().split()
        for i in range(int(s)):
            hx, hy = knots[0]
            knots[0] = move_head(d, hx, hy)
            for k in range(0, n - 1):
                kx, ky = knots[k]
                tx, ty = knots[k + 1]
                knots[k + 1] = sync_tail(kx, ky, tx, ty)
                grid[knots[n - 1]] = True
    return len(grid)


if __name__ == '__main__':
    print(task1())
    print(task2())
