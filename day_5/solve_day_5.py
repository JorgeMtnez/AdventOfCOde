from operator import itemgetter
# Every seat also has a unique seat ID: multiply the row by 8, then add the column.
# In this example, the seat has ID 44 * 8 + 5 = 357.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

SITS_ROWS = [0, 1, 2, 3, 4, 5, 6, 7]


def readFile(fileName: str) -> str:
    my_file = open(fileName, 'r')
    content = my_file.read()
    my_file.close()
    return content


def planeRows() -> list:
    plane_rows = []
    for i in range(0, 128):
        plane_rows.append(i)
    return plane_rows


def idRow(id: str, rows: list) -> int:
    if len(id) == 1:
        if id == "F" or id[0] == "L":
            return rows[0]
        else:
            return rows[1]
    else:
        half = int(len(rows)/2)
        if id[0] == "F" or id[0] == "L":
            return idRow(id[1:len(id)], rows[0:half])
        elif id[0] == "B" or id[0] == "R":
            return idRow(id[1:len(id)], rows[half:(len(rows))])


def part1(content: str) -> list:
    plane_rows = planeRows()
    format_input = content.split("\n")
    sits = {}
    for f in format_input:
        row = idRow(f[0:len(f)-3], plane_rows)
        column = idRow(f[len(f)-3:len(f)], SITS_ROWS)
        id = int(row) * 8 + int(column)
        sits[id] = {'row': row, 'column': column, 'characters': f}
    sorted_sits = sorted(sits.items(), key=lambda x: x[0], reverse=True)
    return sorted_sits

# It's a completely full flight, so your seat should be the only missing boarding pass in your list.
# However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
# so they'll be missing from your list as well.
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
# What is the ID of your seat?


def part2(content: list) -> int:
    end: int = content[0][0]
    free_sits: int = 0
    for c in content:
        if c[0] != end:
            free_sits = int(c[0]) + 1
            # print(c[0])
            end -= 2
        else:
            end -= 1
    print(free_sits)
    return free_sits


def test():
    txt1 = "BFFFBBFRRR"  # row 70, column 7, seat ID 567.
    txt2 = "FFFBBBFRRR"  # row 14, column 7, seat ID 119.
    txt3 = "BBFFBBFRLL"  # row 102, column 4, seat ID 820.
    txt4 = "BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL"
    # print(idRow(txt1[0:len(txt1)-3], planeRows()))
    # print(idRow(txt1[len(txt1)-3:len(txt1)], SITS_ROWS))
    print(part1(txt4))


if __name__ == '__main__':
    print("Exercise 4, part one")
    print(part1((readFile("input.txt")))[0][0])
    print("Exercise 4, part two")
    print(part2(part1((readFile("input.txt")))))
    # test()
