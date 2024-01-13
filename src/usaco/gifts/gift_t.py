"""
ID: ssaad1
LANG: PYTHON3
PROG: gift1
"""

def generate_mapping(l: list[str], n: int) -> dict[str, int]:
  acc : list[str] = []
  for _ in range(n):
    acc.append(l.pop(0))
  return {k: idx for idx, k in enumerate(acc)}

def parse(l: list[str], mapping: dict[str, int]) -> tuple[int, int, list[int]]:
  person = mapping[l.pop(0)]

  temp = l.pop(0).split(' ')
  assert len(temp) == 2
  money = int(temp[0])
  n = int(temp[1])

  people : list[int] = []
  for _ in range(n):
    people.append(mapping[l.pop(0)])

  return (person, money, people)

def read() -> tuple[list[tuple[int, int, list[int]]], int, dict[int, str]]:
  with open("gift.in") as f:
    lines = [x.strip() for x in f.readlines()]
    np = int(lines.pop(0))
    mapping = generate_mapping(lines, np)
    records : list[tuple[int, int, list[int]]] = []

    while lines:
      records.append(parse(lines, mapping))

    return records, np, {v: k for k, v in mapping.items()}

def run() -> dict[str, int]:
  records, n, mapping = read()
  scores = {i: 0 for i in range(n)}

  for person, money, people in records:
    if len(people) == 0:
      continue

    split = money // len(people)
    rem = money - (split * len(people))

    for recipient in people:
      scores[recipient] += split

    scores[person] += rem
    scores[person] -= money
    print(scores)

  return {mapping[i]: v for i, v in scores.items()}

def pprint(res: dict[str, int]) -> None:
  with open("gift.out", "+w") as f:
    for k, v in res.items():
      f.write(f"{k} {v}\n")

pprint(run())