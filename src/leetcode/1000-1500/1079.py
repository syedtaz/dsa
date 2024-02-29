class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        acc : set[str] = set()

        def f(idx: int, prev: str) -> None:
            if idx >= len(tiles):
                return

            yes = prev + tiles[idx]
            acc.add(yes)
            f(idx + 1, yes)
            f(idx + 1, prev)

        f(0, "")
        print(acc)
        return len(acc)

s = Solution()
print(s.numTilePossibilities(tiles = "AAB"))