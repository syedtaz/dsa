from typing import List

def generate(s: str) -> set[str]:
  acc : set[str] = set()

  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      acc.add(s[i:j])

  return acc

def pick_smallest(lst: list[str]) -> str:
  if len(lst) == 0:
    return ""

  lst.sort(key=lambda x: len(x))
  smallest = len(lst[0])
  filtered = [x for x in lst if len(x) == smallest]
  filtered.sort()
  return filtered[0]


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:

      substrings = [generate(x) for x in arr]
      results : list[str] = []

      for i, base in enumerate(substrings):
        current = set([x for x in base])
        for j, other in enumerate(substrings):
            if i == j:
              continue

            for elem in other:
              current.discard(elem)

        results.append(pick_smallest([x for x in current]))

      return results