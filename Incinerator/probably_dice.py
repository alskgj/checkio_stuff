from itertools import product

def probability(num, sides, target):
    total_list = product(range(1, sides+1), repeat=num)
    total = len(list(total_list))
    total_list = product(range(1, sides + 1), repeat=num)
    target = len([e for e in total_list if sum(e) == target])
    print(total, target)
    print()
    return round(target/total, 4)

if __name__ == "__main__":
    print(probability(2, 6, 3))

