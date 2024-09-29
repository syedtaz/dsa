from typing import List, NamedTuple
from collections import defaultdict
from functools import cache


class Choice(NamedTuple):
    idx: int
    score: int


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        def generate_counts(
            letters: list[str], score: list[int]
        ) -> dict[str, list[Choice]]:
            counts: dict[str, list[Choice]] = defaultdict(list)

            for i, ch in enumerate(letters):
                counts[ch].append(Choice(i, score[i]))

            for v in counts.values():
                v.sort(key=lambda x: x.score, reverse=True)

            return counts

        counts = generate_counts(letters=letters, score=score)

        @cache
        def f(i: int) -> int:
            if i >= len(words):
                return 0

            mscore = 0

            for word in words:
                chosen_idxs: set[int] = set()

                for ch in word:
                    if ch not in counts:
                        chosen_idxs.clear()
                        break

                    chosen_curr: Choice | None = None

                    for choice in counts[ch]:
                        if choice.idx not in chosen_idxs and choice.idx >= i:
                            chosen_curr = choice

                    if chosen_curr is None:
                        chosen_idxs.clear()
                        break
                    else:
                        chosen_idxs.add(chosen_curr.idx)

                if len(chosen_idxs) == 0:
                    continue

                value = sum([score[i] for i in chosen_idxs]) + f(max(chosen_idxs) + 1)
                mscore = max(mscore, value)

            return mscore

        return f(0)


s = Solution()
print(
    s.maxScoreWords(
        words=["dog", "cat", "dad", "good"],
        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score=[
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
)
