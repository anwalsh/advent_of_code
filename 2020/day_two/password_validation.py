import os
import sys


def get_input():
    input = []

    with open(os.path.join(sys.path[0], 'input.txt'), "r") as f:
        input = [tuple(map(str, i.rstrip("\n").split(" "))) for i in f]

    return input


def day_one(input):
    valid_count = 0

    for l in input:
        min, max = l[0].split("-")
        char = l[1].rstrip(":")
        password = l[2]
        occurrences = 0

        for x in password:
            if x == char:
                occurrences += 1

        if occurrences >= int(min) and occurrences <= int(max):
            valid_count += 1

    return valid_count


def day_two(input):
    valid_count = 0

    for l in input:
        i_one, i_two = l[0].split("-")
        char = l[1].rstrip(":")
        password = l[2]
        password_list = []

        for e in password:
            password_list.append(e)

        if (password_list[int(i_one)-1] == char and password_list[int(i_two)-1]
            != char) or (password_list[int(i_one)-1] != char and
                         password_list[int(i_two)-1] == char):
            valid_count += 1

    return valid_count


if __name__ == "__main__":
    input = get_input()

    print(f"Day Two, Part One: {day_one(input)}")
    print(f"Day Two, Part Two: {day_two(input)}")
