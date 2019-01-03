import sys

def solve (captcha):
    shift = len(captcha) // 2
    pairs = zip(captcha, captcha[shift:] + captcha[:shift])
    return sum([int(a) for a, b in pairs if a == b])


captcha = sys.argv[1]
print(solve(captcha))
