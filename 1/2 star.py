from util import read_file_to_list

def calculate_calibration_value(lines):
    # Mapping of number words to digits
    number_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    def replace_number_words(line):
        for word, digit in number_words.items():
            line = line.replace(word, digit)
        return line

    total = 0
    for line in lines:
        # Replace spelled-out numbers with digits
        line = replace_number_words(line)

        # Extracting the first and last digit from each line
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit and last_digit:
            # Combining the first and last digit to form a two-digit number
            value = int(first_digit + last_digit)
            total += value

    return total

if __name__ == "__main__":
    lines = read_file_to_list("./1/1 star.txt")

    # Example lines with spelled-out numbers
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    # Calculating the total calibration value
    total_value = calculate_calibration_value(lines)
    print("Total Calibration Value:", total_value)