def parse_game_data(file_path):
    game_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Splitting the line to separate game number and color counts
            parts = line.strip().split(': ')
            game_number = parts[0].split(" ")[1]
            color_counts = parts[1].split('; ')

            # List to hold each iteration's color counts for this game
            game_iterations = []

            # Parsing color counts for each iteration
            for segment in color_counts:
                iteration_data = {}
                colors = segment.split(', ')
                for color in colors:
                    count, color_name = color.split(' ')
                    iteration_data[color_name] = int(count)

                game_iterations.append(iteration_data)

            game_data[game_number] = game_iterations

    return game_data

if __name__ == "__main__":
    # Example usage
    file_path = './day2/example.txt'
    result = parse_game_data(file_path)
    print(result)
