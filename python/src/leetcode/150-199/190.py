class Solution:
    def reverseBits(self, n: int) -> int:
        map: dict[int, int] = {
            5: 0b11111111111111111111111111111111,
            4: 0b11111111000000001111111100000000,
            3: 0b11110000111100001111000011110000,
            2: 0b11001100110011001100110011001100,
            1: 0b10101010101010101010101010101010,
        }

        def f(n: int, i: int) -> int:
            if i == 0:
                return n

            shift = 2 ** (i - 1)
            mask = map[i]
            return f(((n & mask) >> shift) | ((n & mask) << shift), i - 1)

        return f(n, 5)


s = Solution()
s.reverseBits(0b00000010100101000001111010011100)
