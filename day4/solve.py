def task1():
    score = 0
    for line in open('input.txt'):
        first, second = line.strip().split(',')
        first_start, first_end = map(int, first.split('-'))
        second_start, second_end = map(int, second.split('-'))
        if first_start <= second_start and first_end >= second_end:
            score += 1
        elif second_start <= first_start and second_end >= first_end:
            score += 1
    return score


def task2():
    score = 0
    for line in open('input.txt'):
        first, second = line.strip().split(',')
        first_start, first_end = map(int, first.split('-'))
        second_start, second_end = map(int, second.split('-'))
        if first_start > second_end or first_end < second_start:
            continue
        score += 1
    return score


if __name__ == '__main__':
    print(task1())
    print(task2())
