"""
ID: ssaad1
LANG: PYTHON3
TASK: test
"""
from string import ascii_uppercase as upper
# from typing import Callable


def read() -> list[tuple[str, str]]:
    with open("ride.in") as file:
        lines = file.readlines()
        pairs: list[tuple[str, str]] = []
        for i in range(0, len(lines), 2):
            pairs.append((lines[i].strip(), lines[i + 1].strip()))
        return pairs


mapping = {c: idx + 1 for idx, c in enumerate(upper)}


def score(s: str) -> int:
    total = 1
    for c in s:
        total *= mapping[c]
    return total % 47


def result() -> list[str]:
    output: Callable[[tuple[str, str]], str] = (
        lambda x: "GO\n" if score(x[0]) == score(x[1]) else "STAY\n"
    )

    return [output(x) for x in read()]

def output() -> None:

    with open('ride.out', 'w+') as f:
        for s in result():
          f.write(s)

output()