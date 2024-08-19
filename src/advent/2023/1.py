digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digits_rev = {key[::-1]: value for key, value in digits.items()}


def first_digit(line: str) -> tuple[int, int]:
    for i, c in enumerate(line):
        if c.isdigit():
            return i, int(c)
    assert False


def first_word(line: str, mapping: dict[str, int]) -> tuple[int, int]:
    positions = {key: line.find(key) for key in mapping}
    key, idx = min(positions.items(), key=lambda x: x[1])
    return idx, mapping[key]


def first(line: str, mapping: dict[str, int]) -> int:
    ai, a_value = first_digit(line)
    bi, b_value = first_word(line, mapping)
    return a_value if ai < bi else b_value


def read(fname: str) -> list[str]:
    with open(fname, mode="r") as f:
        return f.readlines()


inp = read("1_input_2")
values = [first(line, digits) * 10 + first(line[::-1], digits_rev) for line in inp]
print(sum(values))