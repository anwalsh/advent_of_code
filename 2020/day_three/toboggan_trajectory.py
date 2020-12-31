import os
import sys


def get_input():
    with open(os.path.join(sys.path[0], 'input.txt'), "r") as f:
        tobaggan_run = [line.rstrip("\n")
                        for line in [elem for elem in f.readlines()]]

    return tobaggan_run


def day_one(tobaggan_run):
    return estimate_trees_in_run(tobaggan_run, 1, 3)


def day_two(tobaggan_run):
    return estimate_trees_in_run(tobaggan_run, 1, 1) * estimate_trees_in_run(tobaggan_run, 1, 3) * estimate_trees_in_run(tobaggan_run, 1, 5) * estimate_trees_in_run(tobaggan_run, 1, 7) * estimate_trees_in_run(tobaggan_run, 2, 1)


def estimate_trees_in_run(tobaggan_run, x, y):
    tree_estimate = 0
    row = x
    col = 0

    while row < len(tobaggan_run):
        col += y

        if col >= len(tobaggan_run[row]):
            col = col - (len(tobaggan_run[row]))

        elem = tobaggan_run[row][col]

        if elem == "#":
            tree_estimate += 1

        row += x

    return tree_estimate


if __name__ == "__main__":
    input = get_input()
    print(f"Day Three, Part One: {day_one(input)}")
    print(f"Day Three, Part Two: {day_two(input)}")
