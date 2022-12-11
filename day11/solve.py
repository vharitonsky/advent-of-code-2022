from operator import add, mul


class Item:
    def __init__(self, worry):
        self.worry = worry

    def __eq__(self, other):
        return self is other


class Monkey:
    def __init__(self, items, operation, divby, ontrue, onfalse):
        self.items = items
        self.operation = operation
        self.divby = divby
        self.ontrue = ontrue
        self.onfalse = onfalse
        self.inspections = 0


def parse_monkeyop(operation):
    operation = operation.split('new = ')[-1]
    left, op, right = operation.split()
    op = add if op == '+' else mul
    if right == 'old':
        def monkeyop(x):
            return op(x, x)
    else:
        def monkeyop(x):
            return op(x, int(right))
    return monkeyop


def parse_monkeys():
    items = None
    divby = None
    monkeyop = None
    ontrue = None
    onfalse = None
    monkeyno = -1
    monkeys = []
    for line in open('input.txt'):
        line = line.strip()
        if line.startswith('Monkey'):
            monkeyno += 1
        elif line.startswith('Starting'):
            items = [Item(int(i)) for i in line.split(': ')[-1].split(', ')]
        elif line.startswith('Operation'):
            monkeyop = parse_monkeyop(line)
        elif line.startswith('Test'):
            divby = int(line.split()[-1])
        elif line.startswith('If true'):
            ontrue = int(line.split()[-1])
        elif line.startswith('If false'):
            onfalse = int(line.split()[-1])
        else:
            monkeys.append(Monkey(items, monkeyop, divby, ontrue, onfalse))
    monkeys.append(Monkey(items, monkeyop, divby, ontrue, onfalse))
    return monkeys


def task1(n=20):
    monkeys = parse_monkeys()
    for r in range(n):
        for m in monkeys:
            while m.items:
                item = m.items.pop(0)
                item.worry = round(m.operation(item.worry)//3)
                if item.worry % m.divby == 0:
                    monkeys[m.ontrue].items.append(item)
                else:
                    monkeys[m.onfalse].items.append(item)
                m.inspections += 1
    monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


def task2(n=20):
    monkeys = parse_monkeys()
    common_divby = 1
    for m in monkeys:
        common_divby *= m.divby
    for r in range(n):
        for m in monkeys:
            while m.items:
                item = m.items.pop(0)
                item.worry = m.operation(item.worry)
                if item.worry > common_divby:
                    item.worry = item.worry % common_divby
                if item.worry % m.divby == 0:
                    monkeys[m.ontrue].items.append(item)
                else:
                    monkeys[m.onfalse].items.append(item)
                m.inspections += 1
    monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


if __name__ == '__main__':
    print(task1())
    print(task2(n=10000))
