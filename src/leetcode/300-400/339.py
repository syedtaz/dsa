# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value: None =None) -> None:
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return True

   def add(self, elem: int) -> None:
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value: int) -> None:
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self) -> int | None:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return 1

   def getList(self) -> list['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       return []

from typing import List

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def f(lst: NestedInteger, depth: int) -> int:
            if lst.isInteger():
                v = lst.getInteger()
                assert v  is not None
                return (v * depth)

            l = lst.getList()
            assert l is not None
            return sum([f(x, depth + 1) for x in l])

        return sum([f(x, 1) for x in nestedList])


