def checkio(expression):
    # remove unnecessary stuff
    expression = "".join([e for e in expression if e in "(){}[]"])

    while expression:
        first = [(expression.find(")"), "("),
                 (expression.find("]"), "["),
                 (expression.find("}"), "{")]

        # .find() returns -1 if char isn't found. input is smaller than 10**4
        first = min(first, key=lambda x: x[0] if x[0] > 0 else 10**4)
        close_index, open_char = first

        # closing bracket at start or no closing bracket but expression not empty
        if close_index == 0 or close_index == -1:
            return False

        # try to remove a bracket, if not possible something is wrong
        if expression[close_index-1] == open_char:
            expression = expression[:close_index-1]+expression[close_index+1:]
        else:
            return False

    return True

if __name__ == "__main__":
    print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))



