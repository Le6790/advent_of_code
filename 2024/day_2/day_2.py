"""
https://adventofcode.com/2024/day/2
"""

import sys


def get_input(input_file):
    """
    input - file containing two columns of data
    return - 2 lists of the data

    """
    list_1 = []

    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin.readlines():
            list_1.append(line.strip().split(" "))

    return list_1


def check_level(level):

    # All increasing or all decreasing

    status = "Safe"
    if all(level[i] <= level[i + 1] for i in range(len(level) - 1)):
        print("Ascending")
    elif all(level[i] >= level[i + 1] for i in range(len(level) - 1)):
        print("Descending")
    else:
        print("Neither")
        return "Unsafe"

    if all(
        abs(level[i] - level[i + 1]) >= 1 and abs(level[i] - level[i + 1]) <= 3
        for i in range(len(level) - 1)
    ):
        print("Within range")

    else:
        return "Unsafe"

    return status


def main():
    input = get_input(sys.argv[1])
    print(input)

    safe_count = 0

    for i in input:

        i = list(map(int, i))
        status = check_level(i)
        print(f"{i} is {status}")
        if status == "Safe":
            safe_count += 1

    print(f"Number of safe levels: {safe_count}" )


if __name__ == "__main__":
    main()
