import os
import sys
import re


def get_input():
    with open(os.path.join(sys.path[0], 'input.txt'), "r") as f:
        converted_passports = []
        passports = f.read().split("\n\n")

        for passport in passports:
            passport = passport.replace("\n", " ")

            converted_passports.append(dict((x.strip(), y.strip()) for x, y in (
                element.split(":") for element in passport.split(" "))))

        return converted_passports


def passport_complete(passport):
    valid = True

    if "byr" not in passport or "ecl" not in passport or "eyr" not in passport or "iyr" not in passport or "hcl" not in passport or "hgt" not in passport or "pid" not in passport:
        return not valid

    return valid


def passport_valid(passport):
    valid = True

    if passport_complete(passport):
        if int(passport.get("byr")) < 1920 or int(passport.get("byr")) > 2002:
            return not valid
        if int(passport.get("iyr")) < 2010 or int(passport.get("iyr")) > 2020:
            return not valid
        if int(passport.get("eyr")) < 2020 or int(passport.get("eyr")) > 2030:
            return not valid

        height = passport.get("hgt")

        if "cm" in height or "in" in height:
            if "cm" in height:
                height = height.replace("cm", "")
                if int(height) < 150 or int(height) > 193:
                    return not valid
            if "in" in height:
                height = height.replace("in", "")
                if int(height) < 59 or int(height) > 76:
                    return not valid
        else:
            return not valid

        color_code = re.compile(r"^#[a-f0-9]{6}$")

        if not color_code.match(passport.get("hcl")):
            return not valid

        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if not passport.get("ecl") in valid_colors:
            return not valid

        passport_id = re.compile(r"^[0-9]{9}$")
        if not passport_id.match(passport.get("pid")):
            return not valid

        return valid


def day_one(passports):
    complete_passports = 0

    for passport in passports:
        if passport_complete(passport):
            complete_passports += 1

    return complete_passports


def day_two(passports):
    valid_count = 0

    for passport in passports:
        if passport_valid(passport):
            valid_count += 1

    return valid_count


if __name__ == "__main__":
    passports = get_input()
    print(f"Day Four, Part One: {day_one(passports)}")
    print(f"Day Four, Part Two: {day_two(passports)}")
