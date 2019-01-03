import sys

def solve (captcha):
    pairs = zip(captcha, captcha[1:] + captcha[:1])
    return sum([int(a) for a, b in pairs if a == b])


captcha = sys.argv[1]
print(solve(captcha))
