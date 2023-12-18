def process_card_data(file_path):
    """
    Reads card data from a text file and processes it into a dictionary.

    Args:
    file_path (str): The path to the text file containing the card data.

    Returns:
    dict: A dictionary with card names as keys and another dict as values, 
          where the inner dict contains 'win' and 'have' lists.
    """
    card_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Splitting the line at ':'
            card_name, numbers = line.split(':')
            # Further splitting the numbers into 'win' and 'have' parts
            win_numbers, have_numbers = numbers.split('|')

            # Converting number strings to lists of integers
            win_list = [int(num) for num in win_numbers.split()]
            have_list = [int(num) for num in have_numbers.split()]

            # Adding to the dictionary
            card_dict[card_name.strip()] = {"win": win_list, "have": have_list}

    return card_dict
