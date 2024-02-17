def rand7() -> int:
    return 1

class Solution:
    def rand10(self) -> int:
        x = rand7() * (rand7() - 1) * 7
        return 1 + (x - 1) % 10 if x <= 40 else self.rand10()

