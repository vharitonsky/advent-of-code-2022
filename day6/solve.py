def solve_for_len(seq, window_len):
    window = []
    for i, c in enumerate(seq):
        window.append(c)
        if len(set(window)) == window_len:
            return i + 1
        if len(window) == window_len:
            window.pop(0)


def task1():
    seq = open('input.txt').read().strip()
    return solve_for_len(seq, 4)


def task2():
    seq = open('input.txt').read().strip()
    return solve_for_len(seq, 14)


if __name__ == '__main__':
    print(task1())
    print(task2())
