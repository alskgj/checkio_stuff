def safe_pawns(data: set) -> int:
    protected = {chr(ord(col)+mod) + str(int(row)+1)
                 for col, row in data
                 for mod in [1, -1]}

    return len(data.intersection(protected))



