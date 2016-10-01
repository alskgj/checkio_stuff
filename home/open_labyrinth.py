def checkio(data):
    queue = [((1, 1), "")]  # we will use list for simplicity
    visited = set()

    while queue:
        position, path = queue.pop()
        # found exit
        if position == (10, 10):
            return path
        # position already visited
        if position in visited:
            continue

        y, x = position
        # can't visit position
        if data[y][x] == 1:
            continue

        # append left, up, right, down
        visited.add(position)
        queue.append(((y, x-1), path+"W"))
        queue.append(((y-1, x), path+"N"))
        queue.append(((y, x+1), path+"E"))
        queue.append(((y+1, x), path+"S"))


if __name__ == "__main__":
    ans = checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    print(ans)
