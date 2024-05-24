class Logger:
    seen: dict[str, int]

    def __init__(self) -> None:
        self.seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.seen and timestamp < self.seen[message]:
            return False

        self.seen[message] = timestamp + 10
        return True
