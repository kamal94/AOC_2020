import sys
import re

valid = 0


def valid_hgt(x):
    result = re.search(r"^(\d+)(cm|in)$", x)
    if not result or len(result.groups()) != 2:
        return False
    if result.group(2) == "cm":
        return 150 <= int(result.group(1)) <= 193
    elif result.group(2) == "in":
        return 59 <= int(result.group(1)) <= 76


def valid_hcl(x):
    result = re.search(r"^#[a-fA-F0-9]{6}$", x)
    return result is not None


required_fields = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": valid_hgt,
    "hcl": valid_hcl,
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: re.search(r"^[0-9]{9}$", x) is not None,
}


def debug(x):
    print("XXXXXXXXXXXXXXXX")
    for k, v in x.items():
        print("{}({}):".format(k, v), required_fields[k](v)
              if k in required_fields.keys() else "NA")
    print("XXXXXXXXXXXXXXXX")



def is_valid(x):
    return (len([k for k in required_fields.keys() if k not in current_passport.keys()]) < 1) and \
        (all(required_fields[x](current_passport[x])
             for x in current_passport.keys() if x in required_fields.keys()))


current_passport = {}
for line in sys.stdin:
    line = line.strip()
    if line == "":
        if is_valid(current_passport):
            valid += 1
        # debug(current_passport)
        current_passport = {}
        continue
    props = line.split(" ")
    for prop in props:
        k, v = prop.split(":")
        current_passport[k] = v

# gurad against no new line at the end.
if current_passport:
    if is_valid(current_passport):
        valid += 1
    # debug(current_passport)
    current_passport = {}

print(valid)
