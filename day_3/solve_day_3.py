# Starting at the top-left corner of your map and following a slope of right
# 3 and down 1, how many trees would you encounter?
def readFile(fileName) -> list:
    with open(fileName) as f:
        lines = f.read().splitlines()
    print(lines)
    print(len(lines))
    return lines

def part1(input) -> int:
    free = 0
    tree = 0
    actualPosition = 0
    for line in input:
        print(len(line))
        print(actualPosition)
        if line[actualPosition] == '#':
            tree += 1
            print("hello")
        if (actualPosition + 3) < len(line):
            actualPosition += 3
        elif (actualPosition + 3) >= len(line):
            actualPosition = actualPosition + 3 - len(line)
    return tree

if __name__ == '__main__':
    print("Exercise 3, part one")
    print(part1(readFile("input.txt")))
    # print("Exercise 3, part two")
    # print(part2(readFile("input.txt")))