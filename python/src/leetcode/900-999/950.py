from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        acc: list[int] = [0 for _ in range(len(deck))]
        deck.sort()

        i = 0
        j = 0
        keep = True

        while j < len(acc):

            if acc[i] == 0:

                if keep:
                    acc[i] = deck[j]
                    j += 1

                keep = not keep

            i = (i + 1) % len(acc)

        return acc # type: ignore