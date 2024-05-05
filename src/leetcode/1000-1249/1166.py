from dataclasses import dataclass


@dataclass
class Fd:
    value: int | None
    next: dict[str, "Fd"]


class FileSystem:
    root: Fd

    def __init__(self) -> None:
        self.root = Fd(value=None, next={})

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or path == "":
            return False

        files = path.split("/")[1:]
        print(files)
        current = self.root

        for file in files[:-1]:
            if file not in current.next:
                return False

            current = current.next[file]

        if files[-1] in current.next:
            return False

        current.next[files[-1]] = Fd(value=value, next = {})
        return True

    def get(self, path: str) -> int:
        files = path.split("/")[1:]
        current = self.root

        for file in files:
            if file not in current.next:
                return -1

            current = current.next[file]

        return current.value if current.value is not None else -1