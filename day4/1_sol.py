import sys

valid = 0
required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

current_passport = {}
for line in sys.stdin:
    if line == "\n":
        if len([k for k in required_fields if k not in current_passport.keys()]) < 1:
            valid += 1
            # print("VALID:", current_passport)
        # else:
            # print([k for k in required_fields if k not in current_passport.keys()])
            # print("INVALID:", current_passport)
        current_passport = {}
        continue
    props = line.split(" ")
    for prop in props:
        k, v = prop.split(":")
        current_passport[k] = v

if current_passport:
    if len([k for k in required_fields if k not in current_passport.keys()]) < 1:
        valid += 1
    #     print("VALID:", current_passport)
    # else:
    #     print([k for k in required_fields if k not in current_passport.keys()])
    #     print("INVALID:", current_passport)
    current_passport = {}

print(valid)
