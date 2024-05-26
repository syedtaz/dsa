class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = [x for x in range(1, n + 1)]
        idx : int = 0

        while len(players) > 1:

            kick = (idx + (k - 1)) % len(players)
            players.pop(kick)

            idx = 0 if kick == len(players) else kick

        return players.pop()