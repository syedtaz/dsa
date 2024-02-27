from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        acc: list[str] = []

        for i, (left, right) in enumerate(zip(currentState, currentState[1:])):
            if left == right == "+":
                acc.append(
                    "".join(
                        [
                            "-" if i == j or i + 1 == j else x
                            for j, x in enumerate(currentState)
                        ]
                    )
                )

        return acc