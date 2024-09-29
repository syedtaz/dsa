from typing import List, NamedTuple
from bisect import bisect_right
import heapq


class Candidate:
    id: int
    votes: int
    time: int
    seq: int

    def __init__(self, id: int, votes: int, time: int, seq: int) -> None:
        self.id, self.votes, self.time, self.seq = id, votes, time, seq


Winner = NamedTuple("Winner", [("time", int), ("id", int)])


class TopVotedCandidate:
    winners: list[Winner]

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = self._generate_winners(persons=persons, times=times)

    def _generate_winners(self, persons: List[int], times: List[int]) -> list[Winner]:
        heap = [(time, person) for time, person in zip(times, persons)]
        heapq.heapify(heap)
        state: dict[int, Candidate] = {}
        acc: list[Winner] = []
        seqnum = 0

        def insert_or_add(id: int, time: int, seq: int) -> None:
            if id not in state:
                state[id] = Candidate(id=id, votes=1, time=time, seq=seq)
                return

            state[id].votes += 1
            state[id].time = time
            state[id].seq = seq

        while len(heap) > 0:
            time_min, person_min = heapq.heappop(heap)
            insert_or_add(person_min, time_min, seqnum)
            seqnum += 1

            while len(heap) > 0 and heap[0][0] == time_min:
                _, person = heapq.heappop(heap)
                insert_or_add(person, time_min, seqnum)
                seqnum += 1

            max_votes = max(cand.votes for cand in state.values())
            candidates = [x for x in state.values() if x.votes == max_votes]
            choice = max(candidates, key=lambda x: x.seq)
            acc.append(Winner(time=time_min, id=choice.id))

        return acc

    def q(self, t: int) -> int:
        idx = bisect_right(self.winners, t, key=lambda x: x.time)
        return self.winners[idx - 1].id