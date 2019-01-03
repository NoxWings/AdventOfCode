from sys import stdin
from itertools import combinations

def solve_line (line):
    numbers = [int(n) for n in line.strip().split("\t")]
    for a, b in combinations(numbers, 2):
        if (a % b == 0) or (b % a == 0):
            return max(a, b) // min(a, b)

def solve (matrix):
    return sum(solve_line(line) for line in matrix)

print(solve(stdin))
