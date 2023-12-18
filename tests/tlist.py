from pydsa import list as LL
from typing import TypeVar, List

a = TypeVar('a')

def l2list(lst: List[a]) -> LL.List[a] | None:
  cur = None

  for item in lst:
    cur = LL.insert(cur, item)

  return cur