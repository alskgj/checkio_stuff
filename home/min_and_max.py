
def min(*args, key=None):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key=key)[0]

def max(*args, key=None):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key=key, reverse=True)[0]


if __name__ == "__main__":

    print(min([1, 2, 0, 3, 4]))
