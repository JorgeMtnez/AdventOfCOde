# expecting fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?
def readFile(fileName: str) -> str:
    my_file = open(fileName, 'r')
    content = my_file.read()
    my_file.close()
    return content


def formatInput(content: str) -> list:
    passports = content.split("\n\n")
    dicta = list()
    for passport in passports:
        dicta.append(dict(d.split(":") for d in passport.replace("\n", " ").split()))

    return dicta


def part1(passports: list) -> int:
    valid = 0
    for passport in passports:
        if all(p in passport for p in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",)):
            valid += 1

    return valid

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Count the number of valid passports - those that have all required fields and valid values.
# Continue to treat cid as optional. In your batch file, how many passports are valid?

def part2(passports: list) -> int:
    valid = 0
    for passport in passports:
        if all(p in passport for p in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",)):
            check = 0
            if 1920 <= int(passport["byr"]) <= 2002 and \
                    2010 <= int(passport["iyr"]) <= 2020 and \
                    2020 <= int(passport["eyr"]) <= 2030 and \
                    len(passport["pid"]) == 9 and \
                    passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth") and \
                    len(passport['hcl'].replace("#", "")) == 6 and \
                    "#" in passport['hcl']:

                if "cm" in passport["hgt"] and 150 <= int(passport["hgt"].replace("cm", "")) <= 193:
                    check = 1
                elif "in" in passport["hgt"] and 59 <= int(passport["hgt"].replace("in", "")) <= 76:
                    check = 1
                for f in passport['hcl'].replace("#", ""):
                    if f not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0") and f not in ("a", "b", "c", "d", "e", "f"):
                        check = 0
                for f in passport["pid"]:
                    if f not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                        check = 0
            if check == 1:
                valid += 1
    return valid


def test():
    txt = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f\n\neyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\n\nhcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022\n\niyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
    txt2 = "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\n\niyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946\n\nhcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\n\nhgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007"
    print(part2(formatInput(txt)))

if __name__ == '__main__':
    print("Exercise 4, part one")
    print(part1(formatInput(readFile("input.txt"))))
    print("Exercise 4, part two")
    print(part2(formatInput(readFile("input.txt"))))
    # test()
