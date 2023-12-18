from util import process_card_data


def calculate_intersection_cardinality(card_data):
    """
    Calculates the intersection cardinality between 'win' and 'have' lists for each card.

    Args:
    card_data (dict): A dictionary containing card data.

    Returns:
    dict: A dictionary with card numbers as keys and the cardinality of the intersection as values.
    """
    intersection_cardinality = {}

    for card_name, values in card_data.items():
        # Calculating the intersection between 'win' and 'have' lists
        intersection = set(values['win']).intersection(values['have'])

        # Getting the cardinality (size) of the intersection
        intersection_cardinality[card_name] = len(intersection)

    return intersection_cardinality


def calculate_card_points(intersection_data):
    """
    Calculates the number of points per card based on the intersection cardinality.
    The points double for each number in the intersection, starting at 1 point for 1 number.

    Args:
    intersection_data (dict): A dictionary with the cardinality of the intersection for each card.

    Returns:
    dict: A dictionary with card numbers as keys and the points as values.
    """
    card_points = {}

    for card_name, cardinality in intersection_data.items():
        # Calculating points (2 ** (cardinality - 1)) if cardinality is not zero, else 0
        points = 2 ** (cardinality - 1) if cardinality > 0 else 0
        card_points[card_name] = points

    return card_points


if __name__ == "__main__":
    card_data = process_card_data("day4/data.txt")
    cardinality = calculate_intersection_cardinality(card_data)
    points = calculate_card_points(cardinality)

    points_total = 0
    for key, value in points.items():
        points_total += value

    print(points_total)
