"""
https://adventofcode.com/2024/day/1
"""

import sys


def get_lists(input_file):
    """
    input - file containing two columns of data
    return - 2 lists of the data

    """
    list_1 = []
    list_2 = []

    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin.readlines():
            vals = line.strip().split("  ")
            list_1.append(int(vals[0]))
            list_2.append(int(vals[1]))

    return list_1, list_2


def get_distance(list_1, list_2):
    """
    Problem 1
    Find the distance between the two lists
    by sorting and comparing how  far apart each element is
    at the same index

    """
    # sort the lists
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    # Ensure the lists have the same number of elements
    assert len(list_1) == len(list_2)

    # Calculate the distance as described in the problem
    distance = 0
    for i in range(len(list_1)):
        distance = distance + abs(sorted_list_1[i] - sorted_list_2[i])

    print(f"Total distance: {distance}")
    return distance


def get_similarity_score(list_1, list_2):
    """
    Part 2 
    Provide the similarity score - 
    keep track of how many times an element appears in list 2
    for every element in list 1, multiply it by how many times
    it appears in list two and sum that up for the similarity score
    """
    similarity_score = 0
    list_2_occurances = {}

    for i in list_2:
        if list_2_occurances.get(i) is None:
            list_2_occurances[i] = 1
        else:
            list_2_occurances[i] += 1

    for i in list_1:
        if list_2_occurances.get(i) is not None:
            similarity_score += i * list_2_occurances[i]

    print(f"similarity_score is {similarity_score}")


def main():
    """
    main function
    """
    # Get the lists from input
    list_1, list_2 = get_lists(sys.argv[1])
    get_distance(list_1, list_2)
    get_similarity_score(list_1, list_2)


if __name__ == "__main__":
    main()
