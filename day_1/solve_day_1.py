
# Specifically, they need you to find the two entries that sum to 2020 and
# then multiply those two numbers together.

def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words

def part1(words):
    number = 1
    for w in words:
        num = 2020 - int(w)
        if str(num) in words:
            number = num * number
            # print(num)
    return number

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
# Multiplying them together produces the answer, 241861950.

def part2(words):

    for wor in words:
        for w in words:
            accum = 2020 - int(wor) - int(w)
            if str(accum) in words:
                print(accum)
                return accum * int(wor) * int(w)

if __name__ == '__main__':
    # print("Exercise 1, part one")
    # print(part1(readFile("input.txt")))
    print("Exercise 1, part two")
    print(part2(readFile("input.txt")))