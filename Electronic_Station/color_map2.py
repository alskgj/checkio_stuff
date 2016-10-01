def color_map(region):
    neighbours = dict()
    for i, row in enumerate(region):
        for j, cell in enumerate(row):

            # new entry in neighbours
            if cell not in neighbours:
                neighbours[cell] = set()

            # check all adjacent countries
            if j > 0 and cell != region[i][j - 1]:
                neighbours[cell].add(region[i][j - 1])

            if j < len(row) - 1 and cell != region[i][j + 1]:
                neighbours[cell].add(region[i][j + 1])
            #
            if i > 0 and cell != region[i - 1][j]:
                neighbours[cell].add(region[i - 1][j])

            if i < len(region) - 1 and cell != region[i + 1][j]:
                neighbours[cell].add(region[i + 1][j])

    ####################################################
    # neighbour is a dict containing
    # all countries as keys and all
    # neighbouring countries as values.
    #
    # (0, 0, 0, 3),
    # (0, 1, 1, 1),
    # (0, 0, 2, 0)
    #
    # corresponds to:
    # {0: {1, 2, 3}, 1: {0, 2, 3}, 2: {0, 1}, 3: {0, 1}}
    #####################################################

    color_list = {0, 1, 2, 3}
    colors = dict()

    # plan
    # iterate over every country.
    # if a country has no color assigned choose a color
    # which no adjacent country has

    # initialize empty colors list
    for country in neighbours:
        colors[country] = None

    for country in colors:
        forbidden_colors = set()
        for neighbour in neighbours[country]:
            if colors[neighbour] is not None:
                forbidden_colors.add(colors[neighbour])

        colors[country] = color_list.difference(forbidden_colors).pop()

    solution = list()
    for country in sorted(colors.keys()):
        solution.append(colors[country] + 1)

    return solution


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"


    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True


    assert checker(color_map, (
        (0, 0, 0),
        (0, 1, 1),
        (0, 0, 2),
    )), "Small"
    assert checker(color_map, (
        (0, 0, 2, 3),
        (0, 1, 2, 3),
        (0, 1, 1, 3),
        (0, 0, 0, 0),
    )), "4X4"
    assert checker(color_map, (
        (1, 1, 1, 2, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 0, 1, 1),
        (1, 1, 0, 4, 3, 1),
        (1, 1, 1, 3, 3, 3),
        (1, 1, 1, 1, 3, 5),
    )), "6 pack"

    assert checker(color_map, ((7, 4, 4, 4,), (7, 0, 1, 5,), (7, 2, 3, 5,), (6, 6, 6, 5,),))
