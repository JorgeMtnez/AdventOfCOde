# Each line gives the password policy and then the password. The password
# policy indicates the lowest and highest number of times a given letter must
# appear for the password to be valid. For example, 1-3 a means that the
# password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is
# not; it contains no instances of b, but needs at least 1. The first and
# third passwords are valid: they contain one a or nine c, both within the
# limits of their respective policies.
# How many passwords are valid according to their policies?


# def wrongpart1(dict) -> int:
#     passwords = 0
#     for d in dict:
#         # password -> d
#         # number + letters -> dict[d]
#         numbers, letters = dict[d]
#         counter = d.count(letters)
#         min, max = numbers.split("-")
#         if counter in range(int(min), int(max) + 1):
#             passwords += 1
#
#
#     return passwords

def readFile(fileName) -> list:
    with open(fileName) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines

def part1(list) -> int:
    solution = 0
    for l in list:
        line = l.split(" ")
        number = line[0].split("-")
        letter = line[1].replace(":", "")
        passw = line[2]
        counter = passw.count(letter)
        if counter in range(int(number[0]), int(number[1]) + 1):
            solution += 1
    return solution

# Each policy actually describes two positions in the password, where 1 means
# the first character, 2 means the second character, and so on. (Be careful;
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

def part2(list) -> int:
    solution = 0

    for l in list:
        line = l.split(" ")
        number = line[0].split("-")
        letter = line[1].replace(":", "")
        passw = line[2]
        if ((passw[int(number[0])-1] == letter) ^ (passw[int(number[1])-1] == letter)):
            solution += 1

    return solution


if __name__ == '__main__':
    print("Exercise 2, part one")
    print(part1(readFile("input.txt")))
    print("Exercise 2, part two")
    print(part2(readFile("input.txt")))
