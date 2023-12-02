# https://adventofcode.com/2023/day/1
import sys

# python3 day_1.py inputs/actual_input.txt
def calculate_calibration_sum(calibration_lines):
    calibration_sum = 0
    for line in calibration_lines:
        values = []
        if not line:
            pass
        for char in line:
            if char.isnumeric():
                values.append(char)

        if len(values) != 0:
            calibration_sum += int(values[0] + values[-1])
    return (calibration_sum)


def adjust_calibration_lines(calibration_lines):
    adjusted_calibration_lines = []

    for line in calibration_lines:
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        print(line)
        adjusted_calibration_lines.append(line)

    return adjusted_calibration_lines


def main():
    calibration_document = sys.argv[1]

    calibration_lines = []
    with open(calibration_document, 'r') as doc_in:
        for line in doc_in.readlines():
            if not line:
                pass
            calibration_lines.append(line.strip())

    print(calculate_calibration_sum(calibration_lines))

    adjusted_calibration_lines = adjust_calibration_lines(calibration_lines)

    print(calculate_calibration_sum(adjusted_calibration_lines))


if __name__ == "__main__":
    main()
