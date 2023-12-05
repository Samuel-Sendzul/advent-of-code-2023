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