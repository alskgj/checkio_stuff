numerals = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}

def checkio(inp, output=""):
    next = max([e for e in numerals if numerals[e]<=inp], key=lambda x: numerals[x])
    output = output+next
    inp = inp-numerals[next]
    if inp <= 0:
        return output
    else:
        return checkio(inp, output=output)

if __name__ == "__main__":
        print(checkio(44))