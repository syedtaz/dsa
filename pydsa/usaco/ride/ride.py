"""
ID: ssaad1
LANG: PYTHON3
PROG: ride
"""
from string import ascii_uppercase as upper


def read():
    with open("ride.in") as file:
        lines = file.readlines()
        pairs = []
        for i in range(0, len(lines), 2):
            pairs.append((lines[i].strip(), lines[i + 1].strip()))
        return pairs


mapping = {c: idx + 1 for idx, c in enumerate(upper)}

def score(s):
    total = 1
    for c in s:
        total *= mapping[c]
    return total % 47


def result():
    output = lambda x: "GO\n" if score(x[0]) == score(x[1]) else "STAY\n"
    return [output(x) for x in read()]


def output():
    with open("ride.out", "w+") as f:
        for s in result():
            f.write(s)


output()
