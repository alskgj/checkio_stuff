VOWELS = "aeiouy"


def translate(data):
    solution = ""
    data = list(data)
    while data:
        current = data.pop(0)
        solution = solution+current
        if current in VOWELS:
            data = data[2:]
        elif current == " ":
            continue
        else:
            data = data[1:]
    return solution