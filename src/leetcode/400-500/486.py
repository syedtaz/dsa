from typing import List
from enum import Enum
from dataclasses import dataclass
from functools import cache


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        class Player(Enum):
            A = 0
            B = 1

        @dataclass(frozen=True)
        class State:
            i: int
            j: int
            score: int

        def flip(p: Player) -> Player:
            return Player.B if p == Player.A else Player.A

        def newst(st: State) -> tuple[int, int, int, int, int, int]:
            v1, i1, j1 = nums[st.i : st.j][0], st.i + 1, st.j
            v2, i2, j2 = nums[st.i : st.j][-1], st.i, st.j - 1
            return v1, i1, j1, v2, i2, j2

        def nscore(st: State, v: int, p: Player) -> int:
            return st.score + v if p == Player.A else st.score - v

        @cache
        def play(st: State, p: Player) -> bool:
            match len(nums[st.i : st.j]), p:
                case (0, Player.A):
                    return st.score >= 0
                case (0, Player.B):
                    return st.score < 0
                case _, Player.A | Player.B:
                    v1, i1, j1, v2, i2, j2 = newst(st)
                    if (
                        play(State(i=i1, j=j1, score=nscore(st, v1, p)), flip(p))
                        == False
                        or play(State(i=i2, j=j2, score=nscore(st, v2, p)), flip(p))
                        == False
                    ):
                        return True
                    return False

        return play(State(i=0, j=len(nums), score=0), Player.A)


# s = Solution()
# print(s.predictTheWinner([0]))
# print(s.predictTheWinner([1, 5, 2]))
# print(s.predictTheWinner([1, 5, 233, 7]))
