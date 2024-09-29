from typing import List
import heapq

class Video:
    __slots__ = ("content", "likes", "dislikes", "views")

    content: str
    likes: int
    dislikes: int
    views: int

    def __init__(self, content: str) -> None:
        self.content = content
        self.likes, self.dislikes, self.views = 0, 0, 0


class VideoSharingPlatform:
    videos: dict[int, Video]
    heap : list[int]
    pos: int

    def __init__(self) -> None:
        self.videos = {}
        self.heap = []
        self.pos = 0

    def upload(self, video: str) -> int:

        if len(self.heap) > 0:
            temp = heapq.heappop(self.heap)
        else:
            temp = self.pos
            self.pos += 1

        v = Video(video)
        self.videos[temp] = v
        return temp

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
          self.videos.pop(videoId)
          heapq.heappush(self.heap, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.videos:
            self.videos[videoId].views += 1
            return self.videos[videoId].content[startMinute : endMinute + 1]

        return "-1"

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.videos:
            return [self.videos[videoId].likes, self.videos[videoId].dislikes]

        return [-1]

    def getViews(self, videoId: int) -> int:
        return self.videos[videoId].views if videoId in self.videos else -1
