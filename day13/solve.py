import json


def is_correct(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    if isinstance(left, int) and isinstance(right, list):
        return is_correct([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return is_correct(left, [right])
    if isinstance(left, list) and isinstance(right, list):
        iter_left = iter(left)
        iter_right = iter(right)
        while True:
            try:
                sub_left = next(iter_left)
            except StopIteration:
                if len(left) == len(right):
                    return None
                return True
            try:
                sub_right = next(iter_right)
            except StopIteration:
                if len(left) == len(right):
                    return None
                return False
            sub_correct = is_correct(sub_left, sub_right)
            if sub_correct is None:
                continue
            return sub_correct


def task1():
    f = open('input.txt')
    i = 0
    correct = []
    while True:
        i += 1
        try:
            left, right = next(f), next(f)
        except StopIteration:
            break
        left, right = json.loads(left.strip()), json.loads(right.strip())
        if is_correct(left, right):
            correct.append(i)
        try:
            next(f)
        except StopIteration:
            break
    return sum(correct)


def task2():
    f = open('input.txt')
    all_packets = []
    while True:
        try:
            left, right = next(f), next(f)
        except StopIteration:
            break

        left, right = json.loads(left.strip()), json.loads(right.strip())
        all_packets.append(left)
        all_packets.append(right)
        try:
            next(f)
        except StopIteration:
            break
    all_packets.append([[2]])
    all_packets.append([[6]])
    while True:
        swapped = False
        for i in range(len(all_packets) - 1):
            if not is_correct(all_packets[i], all_packets[i + 1]):
                all_packets[i], all_packets[i + 1] = all_packets[i + 1], all_packets[i]
                swapped = True
        if not swapped:
            break
    correct = []
    for i, p in enumerate(all_packets, start=1):
        if p == [[2]] or p == [[6]]:
            correct.append(i)
    return correct[0] * correct[1]


if __name__ == '__main__':
    print(task1())
    print(task2())
