from collections import defaultdict


def task1():
    forest = []
    for line in open('input.txt'):
        forest.append([int(t) for t in line.strip()])
    visible_trees = set()
    for i, row in enumerate(forest):
        max_tree = -1
        for j, tree in enumerate(row):
            if tree > max_tree:
                visible_trees.add((i, j))
                max_tree = tree
    for i, row in enumerate(forest):
        max_tree = -1
        for j in range(len(row) - 1, -1, -1):
            tree = row[j]
            if tree > max_tree:
                visible_trees.add((i, j))
                max_tree = tree
    for j in range(0, len(forest[0])):
        max_tree = -1
        for i, row in enumerate(forest):
            tree = row[j]
            if tree > max_tree:
                visible_trees.add((i, j))
                max_tree = tree
    for j in range(0, len(forest[0])):
        max_tree = -1
        for i in range(len(forest) - 1, -1, -1):
            row = forest[i]
            tree = row[j]
            if tree > max_tree:
                visible_trees.add((i, j))
                max_tree = tree
    return len(visible_trees)


def task2():
    forest = []
    for line in open('input.txt'):
        forest.append([int(t) for t in line.strip()])
    scenic_scores = defaultdict(lambda: 1)
    for i, row in enumerate(forest):
        trees = []
        for j, tree in enumerate(row):
            scenic_score = 0
            for left_tree in reversed(trees):
                scenic_score += 1
                if tree <= left_tree:
                    break
            scenic_scores[(i, j)] *= scenic_score
            trees.append(tree)

    for i, row in enumerate(forest):
        trees = []
        for j in range(len(row) - 1, -1, -1):
            tree = row[j]
            scenic_score = 0
            for right_tree in trees:
                scenic_score += 1
                if tree <= right_tree:
                    break
            scenic_scores[(i, j)] *= scenic_score
            trees.insert(0, tree)

    for j in range(0, len(forest[0])):
        trees = []
        for i, row in enumerate(forest):
            tree = row[j]
            scenic_score = 0
            for top_tree in reversed(trees):
                scenic_score += 1
                if tree <= top_tree:
                    break
            scenic_scores[(i, j)] *= scenic_score
            trees.append(tree)

    for j in range(0, len(forest[0])):
        trees = []
        for i in range(len(forest) - 1, -1, -1):
            row = forest[i]
            tree = row[j]
            scenic_score = 0
            for bottom_tree in trees:
                scenic_score += 1
                if tree <= bottom_tree:
                    break
            scenic_scores[(i, j)] *= scenic_score
            trees.insert(0, tree)
    return max(scenic_scores.values())


if __name__ == '__main__':
    print(task1())
    print(task2())
