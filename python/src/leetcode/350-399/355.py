from collections import defaultdict
from typing import List
import heapq

tweet = tuple[int, int]


class Twitter:
    clock: int
    following: dict[int, set[int]]
    tweets: dict[int, list[tweet]]

    def __init__(self):
        self.clock = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (self.clock, tweetId))
        self.clock -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        following.add(userId)

        pqueue: list[tweet] = []

        for user in following:
            buffer: list[tweet] = []
            source: list[tweet] = self.tweets.get(user, [])

            if len(source) == 0:
                continue

            for _ in range(min(10, len(source))):
                buffer.append(heapq.heappop(source))

            for item in buffer:
                heapq.heappush(pqueue, item)
                heapq.heappush(source, item)

        acc: list[int] = []

        for _ in range(min(10, len(pqueue))):
            _, id = heapq.heappop(pqueue)
            acc.append(id)

        return acc

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
