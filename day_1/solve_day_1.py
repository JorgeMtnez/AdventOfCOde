
# Specifically, they need you to find the two entries that sum to 2020 and
# then multiply those two numbers together.

def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words
def findSum(words):
    number = 1
    for w in words:
        num = 2020 - int(w)
        if str(num) in words:
            number = num * number
            print(num)
    return number

if __name__ == '__main__':
    print("Hola")
    print(findSum(readFile("input.txt")))