from util import parse_game_data
from typing import Dict


def get_possible_games(games: Dict) -> int:
    # Get all impossible games
    impossible_games = []

    outer_break = False
    for i, game in games.items():
        if outer_break:  # if the flag is set
            break  # Break the outer loop if flag is set
        for pick in game:
            for colour, count in pick.items():
                if colour == "red" and count > 12:
                    impossible_games.append(i)
                    outer_break = True  # Set the flag to break the outer loop
                    break  # Break the inner loop
                if colour == "green" and count > 13:
                    impossible_games.append(i)
                    outer_break = True  # Set the flag to break the outer loop
                    break  # Break the inner loop
                if colour == "blue" and count > 14:
                    impossible_games.append(i)
                    outer_break = True  # Set the flag to break the outer loop
                    break  # Break the inner loop

        # Reset the flag for the next iteration of the outer loop
        outer_break = False

    game_numbers = games.keys()
    possible_games = [
        item for item in game_numbers if item not in impossible_games]

    possible_game_sum = 0
    for game_count in possible_games:
        possible_game_sum += int(game_count)

    return possible_game_sum


if __name__ == "__main__":
    # Example usage
    file_path = './day2/1star.txt'
    games = parse_game_data(file_path)
    possible_game_sum = get_possible_games(games)

    print(possible_game_sum)
