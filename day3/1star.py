from util import read_file_to_list_of_lists


def find_full_numbers_next_to_symbols(grid):
    """
    Find all full numbers that are directly next to a symbol in the grid.
    A symbol is defined as any non-digit and non-period character.

    Args:
    grid (List[List[str]]): The grid as a list of lists.

    Returns:
    Set[str]: A set of all full numbers next to symbols.
    """
    # Define the directions to check for symbols
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Set to store the numbers found next to symbols
    numbers_next_to_symbols = set()

    # Function to get the full number from a starting position
    def get_full_number(row, col):
        number = ''
        # Check left
        c = col
        while c >= 0 and grid[row][c].isdigit():
            number = grid[row][c] + number
            c -= 1

        # Check right
        c = col + 1
        while c < len(grid[row]) and grid[row][c].isdigit():
            number += grid[row][c]
            c += 1

        return number

    # Iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if the current element is a symbol
            if not grid[row][col].isdigit() and grid[row][col] != '.':
                # Check all directions for numbers
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc].isdigit():
                        full_number = get_full_number(nr, nc)
                        numbers_next_to_symbols.add(full_number)

    return numbers_next_to_symbols


if __name__ == "__main__":
    file_path = 'day3/data.txt'  # Replace with your actual file path
    grid_from_file = read_file_to_list_of_lists(file_path)
    part_numbers = find_full_numbers_next_to_symbols(grid_from_file)
    print(sum([int(num) for num in part_numbers]))
