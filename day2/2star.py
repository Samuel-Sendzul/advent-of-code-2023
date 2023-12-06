from typing import Dict
from util import parse_game_data

# Function to calculate the maximum number of each color per key in the outer dict


def calculate_max_colors_per_key(games):
    max_colors = {}
    for key, value in games.items():
        # Initialize a dict to hold the maximum count of each color for this key
        max_colors[key] = {'red': 0, 'green': 0, 'blue': 0}
        for color_set in value:
            for color, count in color_set.items():
                max_colors[key][color] = max(max_colors[key][color], count)
    return max_colors

# Function to calculate the product of the maximum color values for each key in the original dict


def calculate_product_of_max_colors(max_colors):
    product_dict = {}
    for key, color_values in max_colors.items():
        # Calculate the product of the maximum values for red, green, and blue
        product = 1
        for color, value in color_values.items():
            product *= value
        product_dict[key] = product
    return product_dict


def calculate_game_power(games: Dict) -> int:
    # Get max per colour per game
    possible_cubes = calculate_max_colors_per_key(games)

    # Get power per game
    power_per_game = calculate_product_of_max_colors(possible_cubes)

    # Get sum of power
    result = 0
    for key, value in power_per_game.items():
        result += value

    return result


if __name__ == "__main__":
    file_path = './day2/1star.txt'
    games = parse_game_data(file_path)
    power = calculate_game_power(games)
    print(power)
