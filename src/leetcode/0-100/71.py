from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        trimmed = [x for x in path.split("/") if x != ""]
        stack : deque[str] = deque()

        i = len(trimmed) - 1
        while i >= 0:
            match trimmed[i]:
                case '.':
                    i -= 1
                case '..':
                    i -= 2
                case _:
                    stack.appendleft(path[i])
                    i -= 1

        return "/" + "/".join(stack)