class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counts = {x: 0 for x in vowels}
        masks : dict[str, list[int]] = {x: [] for x in vowels}

        for c in s:
            if c in vowels:
                counts[c] += 1
            for k, v in counts.items():
                masks[k].append(1 if v % 2 == 0 else 0)

        acc = masks['a']
        vowels.remove('a')
        for v in vowels:
            acc = acc and masks[v]

        cur = 0
        mseen = 0



        print(acc)

s = Solution()
s.findTheLongestSubstring("leetcodeisgreat")