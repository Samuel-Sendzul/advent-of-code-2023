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
    # Example lines from the prompt
    example_lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]

    # Calculating the total calibration value
    total_value = calculate_calibration_value(example_lines)
    print("Total Calibration Value:", total_value)