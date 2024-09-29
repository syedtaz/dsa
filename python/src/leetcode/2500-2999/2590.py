from typing import NamedTuple, List
from collections import defaultdict
import heapq

Task = NamedTuple(
    "Task", [("due", int), ("id", int), ("descr", str), ("tags", frozenset[str])]
)


class User:
    task_q: list[Task]
    task_map: dict[int, Task]

    def __init__(self) -> None:
        self.task_q = []
        self.task_map = {}


class TodoList:
    state: dict[int, User]
    clock: int

    def __init__(self) -> None:
        self.state = defaultdict(User)
        self.clock = 1

    def addTask(
        self, userId: int, taskDescription: str, dueDate: int, tags: List[str]
    ) -> int:
        curclock = self.clock
        t = Task(due=dueDate, id=curclock, descr=taskDescription, tags=frozenset(tags))
        user = self.state[userId]

        # Mutation
        heapq.heappush(user.task_q, t)
        user.task_map[curclock] = t
        self.clock += 1

        return curclock

    def getAllTasks(self, userId: int) -> List[str]:
        return [task.descr for task in self.state[userId].task_q]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        return [task.descr for task in self.state[userId].task_q if tag in task.tags]

    def completeTask(self, userId: int, taskId: int) -> None:
        user = self.state[userId]

        if taskId not in user.task_map:
            return

        task = user.task_map[taskId]
        idx = user.task_q.index(task)

        _ = user.task_q.pop(idx)
        _ = user.task_map.pop(taskId)
        heapq.heapify(user.task_q)
