from util import read_file_to_list

def calculate_calibration_value(lines: list[str]):
    total = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        total += int(digits[0] + digits[-1])
    return total

if __name__ == "__main__":
    lines = read_file_to_list("./1/1 star.txt")

    # Calculating the total calibration value
    total_value = calculate_calibration_value(lines)
    print("Total Calibration Value:", total_value)