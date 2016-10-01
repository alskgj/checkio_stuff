def create_neighbours(region):
    """neighbour is a dict containing
    all countries as keys and all
    neighbouring countries as values.
    #
    # (0, 0, 0, 3),
    # (0, 1, 1, 1),
    # (0, 0, 2, 0)
    #
    corresponds to:
    # {0: {1, 2, 3}, 1: {0, 2, 3}, 2: {0, 1}, 3: {0, 1}}"""
    neighbours = dict()
    for i, row in enumerate(region):
        for j, cell in enumerate(row):

            # new entry in neighbours
            if cell not in neighbours:
                neighbours[cell] = set()

            # check all adjacent countries
            if j > 0 and cell != region[i][j-1]:
                neighbours[cell].add(region[i][j-1])

            if j < len(row)-1 and cell != region[i][j+1]:
                neighbours[cell].add(region[i][j+1])
            #
            if i > 0 and cell != region[i-1][j]:
                neighbours[cell].add(region[i-1][j])

            if i < len(region)-1 and cell != region[i+1][j]:
                neighbours[cell].add(region[i+1][j])

    return neighbours


def is_solved(neighbours, colors):
    """Checks for all countries, if all their neighbours have another color.

    :param neighbours: A dict with country as keys, list of neighbours as values
    :param colors: A list indicating which country has which color. First element in this list corresponds
    to color of first country
    :return: Boolean
    """
    if None in colors:
        return False
    elif len(neighbours) != len(colors):
        return False

    for country in neighbours:
        color = colors[country]
        for neighbour in neighbours[country]:
            if colors[neighbour] == color:
                return False
    return True


def is_valid(neighbours, colors):
    """Does something similar to is_solved, but also works if not all countries
    have a color assigned yet

    :param neighbours: A dict with country as keys, list of neighbours as values
    :param colors: A list indicating which country has which color or None.
    :return: Boolean
    """
    for country in neighbours:
        color = colors[country]
        for neighbour in neighbours[country]:
            if color is None or colors[neighbour] is None:
                continue
            elif colors[neighbour] == color:
                return False
    return True


def color_map(region):
    possible_colors = [1, 2, 3, 4]
    neighbours = create_neighbours(region)
    colors = [None]*len(neighbours)

    states = [colors]

    while states:
        current_state = states.pop()

        first = current_state.index(None)

        for choosen_color in possible_colors:
            current_state_copy = current_state[:]
            current_state_copy[first] = choosen_color

            if is_solved(neighbours, current_state_copy):
                return current_state_copy

            elif is_valid(neighbours, current_state_copy):
                states.append(current_state_copy)

    return False


if __name__ == "__main__":
    print(color_map((
        (0, 0, 0),
        (0, 1, 1),
        (0, 0, 2)
    )))

    print(color_map((
        (7, 4, 4, 4),
        (7, 0, 1, 5),
        (7, 2, 3, 5),
        (6, 6, 6, 5)
    )))


