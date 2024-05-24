from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        match len(preorder) % 2:
            case 0:
                left = preorder[: len(preorder) // 2]
                right = preorder[len(preorder) // 2 :]
            case 1:
                left = preorder[: len(preorder) // 2]
                right = preorder[len(preorder) // 2 :]
            case _:
                raise Exception
        return all([x > y for x, y in zip(left, left[1:])]) and all(
            [x < y for x, y in zip(right, right[1:])]
        )
