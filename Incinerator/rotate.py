
def rotate(state, cannonballs):
    solution = []
    for offset in range(len(state)):
        if all([state[(ball-offset) % len(state)] for ball in cannonballs]):
            solution.append(offset)
    return solution


if __name__ == "__main__":
    print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]))