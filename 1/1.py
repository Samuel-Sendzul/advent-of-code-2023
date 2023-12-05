def read_file_to_list(file_path):
    """
    Read a text file and append each line as a string to a list.

    :param file_path: Path to the text file.
    :return: List of strings, each representing a line from the file.
    """
    result_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Stripping any trailing newline character and appending to the list
                result_list.append(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return result_list

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
    lines = read_file_to_list("./1/1.txt")

    # Calculating the total calibration value
    total_value = calculate_calibration_value(lines)
    print("Total Calibration Value:", total_value)