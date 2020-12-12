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
def readFile(fileName) -> list:
    my_file = open(fileName, 'r')
    content = my_file.read()
    passports = content.split("\n\n")
    my_file.close()
    print(passports)
    return passports

def part1(passports) -> int:
    aList = []
    for p in passports:
        aList.append(p.replace("\n"," "))
    valid = 0
    for a in aList:
        if 'byr' in a and 'iyr' in a and 'eyr' in a and 'hgt' in a and 'hcl' in a and\
                'ecl' in a and 'pid' in a:
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

def validator(pString) -> bool:
    dictPass = {}


def part2(passports) -> int:
    aList = []
    for p in passports:
        aList.append(p.replace("\n", " "))
    valid = 0
    for a in aList:
        if 'byr' in a and 'iyr' in a and 'eyr' in a and 'hgt' in a and 'hcl' in a and \
                'ecl' in a and 'pid' in a:
            if validator(a):
                valid += 1


    return valid

if __name__ == '__main__':
    # print("Exercise 4, part one")
    # print(part1(readFile("input.txt")))
    print("Exercise 3, part two")
    print(part2(readFile("input.txt")))
