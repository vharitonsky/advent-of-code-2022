def task1():
    x = 1
    op = None
    f = open('input.txt')
    cycle = 0
    cycles = []
    while True:
        cycle += 1
        if cycle in {20, 60, 100, 140, 180, 220}:
            cycles.append(x * cycle)
        if op:
            x += op
            op = None
            continue
        try:
            raw_op = next(f).strip()
        except StopIteration:
            break
        if raw_op == 'noop':
            continue
        op = int(raw_op.strip().split()[-1])
    return sum(cycles)


def task2():
    x = 1
    op = None
    f = open('input.txt')
    cycle = 0
    crt = []
    for i in range(6):
        crt.append(['.'] * 40)
    row = 0
    while True:
        cycle += 1
        if cycle in {41, 81, 121, 161, 201}:
            row += 1
        if (cycle - 1 - row * 40) in (x - 1, x, x + 1):
            crt[row][cycle - 1 - row * 40] = '#'
        if op:
            x += op
            op = None
            continue
        try:
            raw_op = next(f).strip()
        except StopIteration:
            break
        if raw_op == 'noop':
            continue
        op = int(raw_op.strip().split()[-1])
    return '\n'.join(''.join(row) for row in crt)


if __name__ == '__main__':
    print(task1())
    print(task2())
