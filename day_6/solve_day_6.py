
# For each group, count the number of questions to which anyone answered "yes".
# What is the sum of those counts?

def readFile(fileName: str) -> list:
    my_file = open(fileName, 'r')
    content = my_file.read()
    my_file.close()
    formulary = content.split("\n\n")
    return formulary


def part1(formulary: list) -> int:
    forms = []
    for f in formulary:
        forms.append(f.replace("\n", ""))
    count = 0
    for f in forms:
        L = []
        for letter in f:
            if letter not in L:
                L.append(letter)
        count += len(L)
    return count

# For each group, count the number of questions to which everyone answered "yes".
# What is the sum of those counts?


def part2(formulary: list) -> int:
    count = 0
    for f in formulary:
        forms = f.split("\n")
        long = len(forms)
        L = {}
        for form in forms:
            for letter in form:
                if letter not in L:
                    L[letter] = 0
                if letter in L:
                    L[letter] += 1
        for l in L:
            if L[l] == long:
                count += 1
    return count


if __name__ == '__main__':
    print("Exercise 4, part one")
    print(part1(readFile("input.txt")))
    print("Exercise 4, part two")
    print(part2(readFile("input.txt")))
    # test()