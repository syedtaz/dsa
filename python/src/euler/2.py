from typing import Any, Generator


def fib(bound: int) -> Generator[int, Any, None]:
    a, b = 1, 2

    while a < bound:
        yield a
        c = b + a
        a, b = b, c


def main() -> None:
    print(sum([x for x in fib(4_000_000) if x % 2 == 0]))


if __name__ == "__main__":
    main()
