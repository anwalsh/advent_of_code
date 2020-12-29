import os
import sys


def get_input():
    input = []

    with open(os.path.join(sys.path[0], 'input.txt'), "r") as f:
        for e in f.readlines():
            input.append(e.rstrip("\n"))

    return input


def day_one(expense_report):
    for x in expense_report:
        for y in expense_report:
            if int(x) + int(y) == 2020:
                return int(x) * int(y)


def day_two(expense_report):
    for x in expense_report:
        for y in expense_report:
            for z in expense_report:
                if int(x) + int(y) + int(z) == 2020:
                    return int(x) * int(y) * int(z)


if __name__ == "__main__":
    input = get_input()
    print(f"Day One, Part One: {day_one(input)}")
    print(f"Day One, Part Two: {day_two(input)}")
