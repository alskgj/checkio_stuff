"""
You are given a two or more digits number N. For this mission, you should find the smallest positive number of X,
such that the product of its digits is equal to N. If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit.
Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.

Input: A number N as an integer.

Output: The number X as an integer.
"""


def checkio(n):
    digits = range(2, 10)
    queue = [(n, digits, [])]
    solution = set()

    while queue:
        num, checklist, divisors = queue.pop()
        for n in checklist:
            # if n divides num, and isn't equal to num we continue, else we hit the base case
            if num % n == 0 and num != n:
                queue.append((num/n, digits, divisors+[n]))
            elif num % n == 0 and num == n:
                solution.add("".join(map(str, sorted(divisors+[n]))))

    if solution:
        solution = min(map(int, solution))
    else:
        solution = 0
    return solution

if __name__ == "__main__":
    checkio(17)