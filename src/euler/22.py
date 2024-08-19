from string import ascii_uppercase

mapping = {x: idx + 1 for idx, x in enumerate(ascii_uppercase)}

def f(s: str) -> int:
  count = 0
  for x in s:
    if x != '"':
      count += mapping[x]
  return count

with open("0022_names.txt", mode="r") as file:
  contents = sorted([x.strip() for x in file.read().split(",")])
  values = [f(x) * (i + 1) for i, x in enumerate(contents)]
  print(sum(values))
