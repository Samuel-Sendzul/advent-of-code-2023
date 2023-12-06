def read_file_to_list_of_lists(file_path):
    """
    Read a text file and convert it to a list of lists.

    Args:
    file_path (str): Path to the text file.

    Returns:
    List[List[str]]: List of lists where each inner list is a row of characters from the file.
    """
    with open(file_path, 'r') as file:
        # Read the file and split into lines
        lines = file.read().strip().split('\n')
        # Convert each line to a list
        return [list(line) for line in lines]


if __name__ == "__main__":
    # Example usage
    file_path = 'day3/example.txt'  # Replace with your actual file path
    grid_from_file = read_file_to_list_of_lists(file_path)

    print(grid_from_file)
