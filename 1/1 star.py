from util import read_file_to_list

def calculate_calibration_value(lines):
    total = 0
    for line in lines:
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

    # Calculating the total calibration value
    total_value = calculate_calibration_value(lines)
    print("Total Calibration Value:", total_value)