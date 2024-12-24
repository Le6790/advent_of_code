# https://adventofcode.com/2023/day/2/
import sys
import re


def get_input(input_file):
    lines = []
    with open(input_file, 'r') as fin:
        for line in fin.readlines():
            lines.append(line.strip())

    return lines


def check_if_game_is_valid(game, red_limit, blue_limit, green_limit):
    # Figure out how to get the associated color's count.

    list_of_plays = game.split(':')[1].split(';')

    is_valid = True

    for play in list_of_plays:
        # print(f"play: {play}")
        red = 0
        blue = 0
        green = 0

        red_regex = re.search(r"(\d+) red", play)
        blue_regex = re.search(r"(\d+) blue", play)
        green_regex = re.search(r"(\d+) green", play)

        if (red_regex):
            red = int(red_regex.groups()[0])
        if (blue_regex):
            blue = int(blue_regex.groups()[0])
        if (green_regex):
            green = int(green_regex.groups()[0])
        # print("----")
        # print(f"red is: {red}")
        # print(f"blue is: {blue}")
        # print(f"green is: {green}")
        if red > red_limit or blue > blue_limit or green > green_limit:
            is_valid = False

    return is_valid


def main():
    input_file = sys.argv[1]

    red_limit = 12
    green_limit = 13
    blue_limit = 14

    games = get_input(input_file)

    valid_game_sum = 0

    for game in games:
        game_number = int(re.search(r"^Game (\d+)", game).group(1))
        is_valid = check_if_game_is_valid(
            game, red_limit, blue_limit, green_limit)
        if is_valid:
            print(f"game {game_number} is valid!")
            valid_game_sum += game_number

    print(f"Result: {valid_game_sum}")


if __name__ == "__main__":
    main()
