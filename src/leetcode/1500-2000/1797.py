class AuthenticationManager:
    ttl: int
    state: dict[str, int]

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.state = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.state[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.state:
            return

        if self.state[tokenId] <= currentTime:
            _ = self.state.pop(tokenId)
            return

        self.generate(tokenId=tokenId, currentTime=currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        to_remove = [k for k, v in self.state.items() if v <= currentTime]
        for k in to_remove:
            _ = self.state.pop(k)

        return len(self.state)
