from functools import cache

BOUND = 20

@cache
def f(i: int, j: int) -> int:

  if i > BOUND or j > BOUND:
    return 0

  if i == BOUND and j == BOUND:
    return 1

  return f(i + 1, j) + f(i, j + 1)

def main() -> None:
  print(f(0, 0))

if __name__ == "__main__":
  main()