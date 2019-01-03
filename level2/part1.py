from sys import stdin

def solveLine (line):
    numbers = [int(n) for n in line.strip().split("\t")]
    return max(numbers) - min(numbers)

def solve (matrix):
    return sum(solveLine(line) for line in matrix)

print(solve(stdin))
