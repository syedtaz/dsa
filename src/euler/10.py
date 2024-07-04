from typing import Any, Generator


def sieve(bound: int) -> Generator[int, Any, None]:
    ps = [True] * bound

    for i in range(2, bound):
        if ps[i]:
            yield i
            for j in range(i * i, bound, i):
                ps[j] = False


def main() -> None:
    print(sum(list(sieve(2_000_000))))


if __name__ == "__main__":
    main()
