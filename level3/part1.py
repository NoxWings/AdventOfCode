import sys
from math import sqrt

def get_layer(n):
    return (sqrt(n-1)+1) // 2

def get_pos(n):
    layer = get_layer(n)
    power = (2 * layer) - 1
    pos = n - (power * power)
    print("layer", layer)
    print("power", power)
    print("pos", pos)
    print("posMod", pos % 8)

def solve(n):
    return get_pos(int(n))

print(solve(sys.argv[1]))
