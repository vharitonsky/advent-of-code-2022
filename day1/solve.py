def task1():
    sums_of_calories = [0]
    i = 0
    sum_of_calories = 0
    for line in open('input.txt'):
        if line.strip():
            sum_of_calories += int(line.strip())
            sums_of_calories[i] = sum_of_calories
        else:
            i += 1
            sum_of_calories = 0
            sums_of_calories.append(sum_of_calories)
    return max(sums_of_calories)


def task2():
    sums_of_calories = [0]
    i = 0
    sum_of_calories = 0
    for line in open('input.txt'):
        if line.strip():
            sum_of_calories += int(line.strip())
            sums_of_calories[i] = sum_of_calories
        else:
            i += 1
            sum_of_calories = 0
            sums_of_calories.append(sum_of_calories)
    return sum(sorted(sums_of_calories)[-3:])


if __name__ == '__main__':
    print(task1())
    print(task2())
