def f(delg: list[int], p: int) -> list[int]:
    match len(delg):
        case 0:
            return []
        case _:
          pivot = delg[0]
          yes: list[int] = [x for x in delg if x == pivot]
          no: list[int] = [x for x in delg if x != pivot]
          return yes if len(yes) >= p else f(no, p)

D = []
print(f(D, 0))