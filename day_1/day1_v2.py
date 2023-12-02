import re
import sys


def word_to_val(word):
    match word:
        case "one": return "1"
        case "two": return "2"
        case "three": return "3"
        case "four": return "4"
        case "five": return "5"
        case "six": return "6"
        case "seven": return "7"
        case "eight": return "8"
        case "nine": return "9"
    return word


def calculate_calibration_sum(calibration_lines):
    sum = 0

    for line in calibration_lines:
        matches = re.findall(
            "(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))", line)
        if len(matches) > 0:
            sum += int(word_to_val(matches[0]) + word_to_val(matches[-1]))

    return sum


def main():
    calibration_document = sys.argv[1]

    calibration_lines = []
    with open(calibration_document, 'r') as doc_in:
        for line in doc_in.readlines():
            if not line:
                pass
            calibration_lines.append(line.strip())

    print(calculate_calibration_sum(calibration_lines))


if __name__ == "__main__":
    main()
