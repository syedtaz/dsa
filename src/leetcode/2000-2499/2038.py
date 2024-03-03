class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        def moves(s: str, A: bool) -> int:
            if len(s) < 3:
                return 0

            target = 'A' if A else 'B'
            acc : int = 0
            for a, b, c in zip(s, s[1:], s[2:]):
                if a == b == c == target:
                    acc += 1
            return acc

        alice = moves(colors, True)
        bob = moves(colors, False)
        return alice - bob > 0