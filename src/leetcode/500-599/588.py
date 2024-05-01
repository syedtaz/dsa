from sortedcontainers import SortedDict
from dataclasses import dataclass
from typing import List

@dataclass
class File:
    contents: str

@dataclass
class Directory:
    files: SortedDict


class FileSystem:
    fs: Directory

    def __init__(self) -> None:
        self.fs = Directory(SortedDict())

    def __traverse__(self, path: list[str], create: bool = False) -> Directory:
        current = self.fs

        for node in path:
            if create and (node not in current.files):
                current.files[node] = Directory(SortedDict())
            current = current.files[node]

        return current


    def ls(self, path: str) -> List[str]:
        stack = [x for x in path.split("/") if x != ""]
        node = self.__traverse__(stack)

        if type(node) == Directory:
            return node.files.keys()

        return [stack.pop()]


    def mkdir(self, path: str) -> None:
        stack = [x for x in path.split("/") if x != ""]
        print(stack)
        _ = self.__traverse__(stack, create=True)


    def addContentToFile(self, filePath: str, content: str) -> None:
        stack = [x for x in filePath.split("/") if x != ""]
        filename = stack.pop()
        dir = self.__traverse__(stack, create=True)

        if filename not in dir.files:
            dir.files[filename] = File(contents=content)
            return None

        dir.files[filename].contents += content
        return None


    def readContentFromFile(self, filePath: str) -> str:
        stack = [x for x in filePath.split("/") if x != ""]
        filename = stack.pop()
        dir = self.__traverse__(stack)
        return dir.files[filename].contents