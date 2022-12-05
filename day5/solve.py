
class Stack:

    def __init__(self, boxes):
        self.boxes = boxes

    def put(self, box):
        if self.boxes[0] != '':
            self.boxes = [box] + self.boxes
            return
        for i, _ in enumerate(self.boxes):
            if i == len(self.boxes) - 1:
                self.boxes[i] = box
                return
            if self.boxes[i + 1] != '':
                self.boxes[i] = box
                return

    def get(self):
        for i, c in enumerate(self.boxes):
            if c != '':
                self.boxes[i] = ''
                return c

    def __str__(self):
        return '\n'.join(f'[{b}]' for b in self.boxes)


def parse_stacks():
    stack_lines = []
    number_line = ''
    for line in open('input.txt'):
        if '1' in line:
            number_line = line
            break
        stack_lines.append(line)
    stacks = []
    for i, c in enumerate(number_line):
        if c.isdigit():
            boxes = []
            for k, line in enumerate(stack_lines):
                if len(line) < i:
                    boxes.append('')
                else:
                    boxes.append(line[i].strip())
            stacks.append(Stack(boxes))
    return stacks


def parse_instructions():
    """move 6 from 1 to 7"""
    instructions = []
    f = open('input.txt')
    for line in f:
        if not line.strip():
            break
    for line in f:
        numbers = []
        for c in line.split():
            if c.isdigit():
                numbers.append(int(c))
        instructions.append(numbers)
    return instructions


def task1():
    stacks = parse_stacks()
    instructions = parse_instructions()
    for what, fr, to in instructions:
        for i in range(what):
            stacks[to - 1].put(stacks[fr - 1].get())
    return ''.join(s.get() for s in stacks)


def task2():
    stacks = parse_stacks()
    instructions = parse_instructions()
    for what, fr, to in instructions:
        boxes = []
        for i in range(what):
            boxes.append(stacks[fr - 1].get())
        for b in reversed(boxes):
            stacks[to - 1].put(b)
    return ''.join(s.get() for s in stacks)


if __name__ == '__main__':
    print(task1())
    print(task2())
