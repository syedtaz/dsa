class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pair = tuple[str, int]

        def counts(start: int) -> tuple[str, int, int]:
            ch, idx, count = s[start], start, 0
            while idx <= len(s) - 1 and s[idx] == ch and count < k:
                idx += 1
                count += 1
            return ch, idx, count

        def convert(input: str) -> list[pair]:
            pairs: list[pair] = []
            idx = 0
            while idx < len(s):
                ch, next, count = counts(idx)
                pairs.append((ch, count))
                idx = next
            return pairs

        def collapse(pairs: list[pair]) -> list[pair]:
            ans: list[pair] = []
            ch, count = pairs[0]
            for nch, ncount in pairs[1:] + [("", 0)]:
                if ch == nch:
                    count += ncount
                else:
                    ans.append((ch, count))
                    ch = nch
                    count = ncount
            return ans

        def mapping(pairs: list[pair]) -> list[pair]:
            ans: list[pair] = []
            print(pairs)
            for ch, count in pairs:
                if count < k:
                    ans.append((ch, count))
                else:
                    ncount = count - ((count // k) * k)
                    if ncount > 0:
                        ans.append((ch, ncount))
            return collapse(ans)

        # def fixpoint(prev: str) -> str:
        #     next = mapping(prev, [], k)
        #     return next if prev == next else fixpoint(next)
        print(mapping(convert(s)))
        return ""


s = Solution()
print(s.removeDuplicates(s="pbbcggttciiippooaais", k=2))
